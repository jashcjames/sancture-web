(function(){
  var flow=document.querySelector('.flow');if(!flow)return;
  var $=function(s){return flow.querySelector(s)},
      pin=$('.pin'),world=$('.world'),svg=$('svg'),pack=$('.packet'),plabel=pack.querySelector('span'),
      grid=$('.gridbg'),blobs=$('.blobs'),hero=$('.hero-copy'),caps=[].slice.call(flow.querySelectorAll('.cap'));
  var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  var ic=function(d){return '<svg viewBox="0 0 24 24" aria-hidden="true">'+d+'</svg>'};
  var I={
    doc:'<path d="M7 3h7l4 4v14H7z"/><path d="M14 3v4h4M9.5 12h5M9.5 16h5"/>',
    send:'<path d="M3 11l18-8-8 18-2-8z"/>',
    scan:'<path d="M4 8V4h4M16 4h4v4M20 16v4h-4M8 20H4v-4M7 12h10"/>',
    shield:'<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
    swap:'<path d="M4 7h11M11 3l4 4-4 4M20 17H9M13 13l-4 4 4 4"/>',
    user:'<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/>',
    file:'<path d="M7 3h7l4 4v14H7z"/><path d="M9 14l2.5 2.5L16 12"/>',
    chart:'<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    rupee:'<path d="M7 5h10M7 9h10M7 5c6 0 6 8 0 8l8 6"/>'
  };
  var chip=function(a,b){return '<div class="chip"><span>'+a+'</span><span>'+b+'</span></div>'};
  var N=[
    {t:'Issue invoice',s:'Business \u00B7 Sales',i:'doc',b:chip('INV-1042','\u20B948,500')+'<div class="bars"><i></i><i></i><i></i></div>'},
    {t:'Send documents',s:'Email or WhatsApp to Sancture',i:'send',b:chip('Invoices.pdf','Sent')+chip('Bank.csv','Sent')+chip('Purchases.xlsx','Sent')},
    {t:'Scan documents',s:'Read invoice data',i:'scan',b:'<div class="meter"><i></i></div>'+chip('Invoices read','128')},
    {t:'Verify entries',s:'GSTIN, HSN and tax rates',i:'shield',b:chip('GSTIN','Valid')+chip('Tax rates','Match')},
    {t:'Reconcile',s:'GSTR-2B and AIS matching',i:'swap',b:'<div class="meter"><i></i></div>'+chip('Mismatches','Resolved')},
    {t:'Professional review',s:'Checked before filing',i:'user',b:chip('Reviewer sign-off','Approved')},
    {t:'File return',s:'GST Returns \u00B7 Income Tax Returns',i:'file',b:chip('Acknowledgment','Generated')+chip('Tax payable','Summarised')},
    {t:'Trusted by 250+ clients',s:'Numbers that build confidence',i:'chart',cls:'wide trust',b:'<div class="stats"><div class="stat"><strong data-count="3" data-suf="+">3+</strong><span>Years of experience</span></div><div class="stat"><strong data-count="250" data-suf="+">250+</strong><span>Clients served</span></div><div class="stat"><strong data-count="375" data-pre="\u20B9" data-suf="Cr+">\u20B9375Cr+</strong><span>Supplies processed</span></div></div>'},
    {t:'Payment received',s:'UPI or bank transfer',i:'rupee',b:chip('Service fee','Paid')+chip('GST invoice','Sent')}
  ];
  var L=['Invoices','Documents received','Data extracted','Entries verified','Reconciled','Approved return','Return filed','Fee invoice'];
  var nodes=N.map(function(n){
    var d=document.createElement('div');d.className='node'+(n.cls?' '+n.cls:'');
    d.innerHTML='<div class="nh"><span class="ic">'+ic(I[n.i])+'</span><div><h3>'+n.t+'</h3><p>'+n.s+'</p></div><span class="st" data-s="idle"></span></div><div class="nb">'+n.b+'</div>';
    world.appendChild(d);return d;
  });
  var sts=nodes.map(function(n){return n.querySelector('.st')});

  function counters(){
    [].forEach.call(flow.querySelectorAll('[data-count]'),function(el){
      var to=+el.dataset.count,pre=el.dataset.pre||'',suf=el.dataset.suf||'',t0=performance.now();
      (function s(t){var p=Math.min((t-t0)/1600,1),e=1-Math.pow(1-p,3);el.textContent=pre+Math.round(to*e)+suf;if(p<1)requestAnimationFrame(s)})(t0);
    });
  }

  if(reduce){
    flow.classList.add('static');
    sts.forEach(function(s){s.dataset.s='done'});
    nodes.forEach(function(n){n.classList.add('go')});
    return;
  }

  // svg connectors
  var NS='http://www.w3.org/2000/svg',base=[],prog=[],ports=[],len=[];
  function mk(t,c){var e=document.createElementNS(NS,t);if(c)e.setAttribute('class',c);svg.appendChild(e);return e}
  for(var i=0;i<N.length-1;i++){base.push(mk('path','base'));prog.push(mk('path','prog'))}
  for(i=0;i<(N.length-1)*2;i++)ports.push(mk('circle','port'));

  var vw,vh,mob,anchor,cx=[],cyv=[],W=[];
  function layout(){
    vw=innerWidth;vh=innerHeight;mob=vw<860;
    var nw=mob?230:280,tw=mob?300:440,gap=mob?70:120,cy=vh*(mob?.73:.52),
        yo=[0,-60,50,-50,50,-40,40,0,-20].map(function(v){return v*(mob?.55:1)});
    anchor=vw*(mob?.5:.66);
    var c=anchor,right=0;
    nodes.forEach(function(n,i){
      var w=n.classList.contains('wide')?tw:nw;W[i]=w;
      if(i)c+=W[i-1]/2+gap+w/2;
      cx[i]=c;n.style.width=w+'px';n.style.left=(c-w/2)+'px';
      var h=n.offsetHeight;cyv[i]=cy+yo[i];n.style.top=(cyv[i]-h/2)+'px';right=c+w/2;
    });
    var tot=right+vw;
    world.style.width=tot+'px';svg.setAttribute('width',tot);svg.setAttribute('height',vh);
    for(var i=0;i<N.length-1;i++){
      var x1=cx[i]+W[i]/2,y1=cyv[i],x2=cx[i+1]-W[i+1]/2,y2=cyv[i+1],dx=(x2-x1)*.5,
          d='M'+x1+' '+y1+' C'+(x1+dx)+' '+y1+' '+(x2-dx)+' '+y2+' '+x2+' '+y2;
      base[i].setAttribute('d',d);prog[i].setAttribute('d',d);
      len[i]=prog[i].getTotalLength();
      prog[i].style.strokeDasharray=len[i];
      [[ports[i*2],x1,y1],[ports[i*2+1],x2,y2]].forEach(function(p){p[0].setAttribute('cx',p[1]);p[0].setAttribute('cy',p[2]);p[0].setAttribute('r',5)});
    }
  }
  layout();addEventListener('resize',layout);
  if(document.fonts&&document.fonts.ready)document.fonts.ready.then(layout);

  var cl=function(v,a,b){return Math.min(Math.max(v,a),b)},ss=function(x){return x*x*(3-2*x)};
  var h=0,vis=true,counted=false,lastSeg=-1,lastCap=-2,lastNight=false;
  new IntersectionObserver(function(e){vis=e[0].isIntersecting},{rootMargin:'100px'}).observe(flow);

  function frame(){
    requestAnimationFrame(frame);
    if(!vis||document.hidden)return;
    var r=flow.getBoundingClientRect(),p=cl(-r.top/(r.height-vh),0,1),target=p*(N.length-1);
    h+=(target-h)*.14;if(Math.abs(target-h)<.0005)h=target;

    var seg=cl(Math.floor(h),0,N.length-2),f=cl(h-seg,0,1),e=ss(f);
    var pt=prog[seg].getPointAtLength(len[seg]*e);
    pack.style.transform='translate3d('+pt.x+'px,'+pt.y+'px,0)';
    pack.style.opacity=h>.04&&h<N.length-1.02?1:0;
    plabel.style.opacity=ss(cl((f-.12)/.2,0,1))*ss(cl((.88-f)/.2,0,1));
    if(seg!==lastSeg){plabel.textContent=L[seg];lastSeg=seg}
    var headX=cx[seg]+(cx[seg+1]-cx[seg])*e,pan=Math.max(0,headX-anchor);
    world.style.transform='translate3d('+(-pan)+'px,0,0)';
    grid.style.backgroundPosition=(-pan)+'px 0';
    blobs.style.transform='translate3d('+(-pan*.3)+'px,0,0)';

    nodes.forEach(function(n,i){
      var rv=i?ss(cl(h-i+1.4,0,1)):1,st=h>i+.5?'done':(h>i-.15?'run':'idle');
      n.style.opacity=rv;n.style.transform='translateY('+((1-rv)*30)+'px) scale('+(.95+.05*rv)+')';
      if(sts[i].dataset.s!==st){sts[i].dataset.s=st;n.classList.toggle('go',st!=='idle')}
    });
    for(var i=0;i<prog.length;i++)prog[i].style.strokeDashoffset=len[i]*(1-cl(h-i,0,1));

    var ho=1-cl((h-.15)/.55,0,1);
    hero.style.opacity=ho;hero.style.transform=(mob?'':'translateY(-50%) ')+'translateX('+(-40*(1-ho))+'px)';
    hero.style.pointerEvents=ho>.5?'auto':'none';
    var ci=h<.8?-1:h<1.9?0:h<4.9?1:h<6.55?2:h<7.5?3:4;
    if(ci!==lastCap){caps.forEach(function(c,k){c.classList.toggle('on',k===ci)});lastCap=ci}
    var night=h>6.55;if(night!==lastNight){pin.classList.toggle('night',night);lastNight=night}
    if(!counted&&h>6.6){counted=true;counters()}
  }
  frame();
})();
