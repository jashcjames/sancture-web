D="https://www.sancture.in"  # replace with your custom domain
EMAIL="hello@sancture.in"; PHONE="+91 00000 00000"; WA="910000000000"
NAV=[("index.html","Home"),("services.html","Services"),("pricing.html","Pricing"),("blogs.html","Blogs"),("contact.html","Contact us")]
def head(page,title,desc,extra=""):
    nav="".join('<li><a href="%s"%s>%s</a></li>'%(h,' aria-current="page"' if h==page else '',t) for h,t in NAV[:-1])
    return f'''<!DOCTYPE html>
<html lang="en-IN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{D}/{'' if page=='index.html' else page}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website"><meta property="og:url" content="{D}/{page}">
<meta name="theme-color" content="#0E2246">
<link rel="icon" href="assets/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,650;12..96,700&family=Instrument+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">{extra}
</head><body>
<a class="skip" href="#main">Skip to content</a><div class="progress" aria-hidden="true"></div>
<header class="nav"><div class="wrap"><a class="brand" href="index.html" aria-label="Sancture home"><img src="assets/logo.png" alt="" width="40" height="40">Sancture</a>
<button class="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
<ul class="links">{nav}<li><a class="btn" href="contact.html">Book a consultation</a></li></ul></div></header>
<main id="main">'''
FOOT=f'''</main>
<footer><div class="wrap"><div class="cols">
<div><a class="brand" href="index.html"><img src="assets/logo.png" alt="" width="40" height="40">Sancture</a><p>GST and income tax return filing, notices and litigation support for businesses and individuals across India.</p></div>
<div><h3>Services</h3><a href="services.html#gst-returns">GST return filing</a><a href="services.html#itr">Income tax return filing</a><a href="services.html#gst-litigation">GST litigation</a><a href="services.html#it-litigation">Income tax litigation</a></div>
<div><h3>Company</h3><a href="pricing.html">Pricing</a><a href="blogs.html">Blogs</a><a href="contact.html">Contact us</a></div>
<div><h3>Reach us</h3><a href="mailto:{EMAIL}">{EMAIL}</a><a href="tel:{PHONE.replace(' ','')}">{PHONE}</a></div>
</div><small>&copy; 2026 Sancture. All rights reserved. Information on this site is general and not a substitute for professional advice on your specific case.</small></div></footer>
<a class="wa" href="https://wa.me/{WA}" rel="noopener">Chat on WhatsApp</a>
<script src="js/main.js"></script>
'''
import re
def cap(h):
    def t(s):
        s=re.sub(r'\b[Ii]ncome [Tt]ax\b','Income Tax',s)
        s=re.sub(r'\b(GST|Income Tax|[Tt]ax) (return)(s?)\b',lambda k:('Tax' if k.group(1).lower()=='tax' else k.group(1))+' Return'+k.group(3),s)
        s=s.replace('Return filing','Return Filing')
        return re.sub(r'\b[Ll]itigation\b','Litigation',s)
    h=re.sub(r'>([^<]+)<',lambda m:'>'+t(m.group(1))+'<',h)
    return re.sub(r'content="([^"]*)"',lambda m:'content="'+t(m.group(1))+'"',h)
def w(n,s):
    if n.endswith('.html'): s=cap(s)
    open(n,"w",encoding="utf-8").write(s)

# ---------- HOME ----------
ld='''<script type="application/ld+json">{"@context":"https://schema.org","@type":"ProfessionalService","name":"Sancture","url":"%s","logo":"%s/assets/logo.png","description":"GST and Income Tax return filing, notices, appeals and Litigation support.","areaServed":"IN","serviceType":["GST Return Filing","Income Tax Return Filing","GST Litigation","Income Tax Litigation"]}</script>'''%(D,D)
home=head("index.html","Sancture | GST & Income Tax Return Filing and Litigation Experts","Sancture files GST and Income Tax Returns and handles notices, appeals and Litigation. Transparent pricing, on-time filing and expert representation for businesses and individuals in India.",ld)
home+='''
<section class="flow" aria-label="How Sancture works"><div class="pin">
<div class="blobs" aria-hidden="true"></div><div class="gridbg" aria-hidden="true"></div>
<div class="world" aria-hidden="true"><svg></svg><div class="packet"><span>Invoices</span></div></div>
<div class="hero-copy">
<h1>Tax Returns and Compliance <span>filed right with ease.</span></h1>
<p class="kicker">GST AND INCOME TAX</p>
<p>Sancture files your GST and Income Tax Returns and defends you when a notice arrives. Send your documents once and we handle the filing, reconciliation and representation.</p>
<div class="cta"><a class="btn" href="contact.html">Get a free consultation</a><a class="btn ghost" href="pricing.html">See pricing</a></div>
<ul class="chips"><li>GST Returns</li><li>Income Tax Returns</li><li>Notice Replies</li><li>Litigation</li></ul></div>
<div class="cap"><h2>You issue the invoices. We take over the compliance.</h2><p>Share sales invoices, purchase bills and bank statements by email or WhatsApp. Our team confirms receipt the same day and tells you exactly what is missing.</p></div>
<div class="cap"><h2>Every document is checked before it reaches a return.</h2><p>Four services, one workflow, handled by qualified professionals.</p><ul class="chips"><li>GST Returns</li><li>Income Tax Returns</li><li>GST Litigation</li><li>Income Tax Litigation</li></ul><div class="cta"><a class="btn" href="services.html">Explore services</a></div></div>
<div class="cap"><h2>Filed on time. Acknowledged in writing.</h2><p>A reviewer signs off on every return before it is filed. You receive the acknowledgment with a plain summary of the tax payable or the refund due.</p></div>
<div class="cap"><h2>Trusted with real numbers, year after year.</h2><p>Our clients range from first-time filers to growing GST-registered businesses.</p></div>
<div class="cap"><h2>Fixed fees. No surprises on the invoice.</h2><p>Every plan is published and invoiced with GST. Pay by UPI or bank transfer once the work is done.</p><div class="cta"><a class="btn light" href="pricing.html">View pricing</a></div></div>
</div></section>

<section class="sec" style="margin-top:-40px;border-radius:40px 40px 0 0"><div class="wrap">
<div class="head rv"><h2>Simple pricing, published upfront</h2><p>Plans for every stage, from Nil Returns to full Litigation support.</p></div>
<div class="grid">
<article class="card rv"><h3>GST Returns</h3><p>From \u20B9349 per month</p><p><a href="pricing.html">See GST plans</a></p></article>
<article class="card rv"><h3>Income Tax Returns</h3><p>From \u20B9999 per return</p><p><a href="pricing.html">See Income Tax plans</a></p></article>
<article class="card rv"><h3>Litigation</h3><p>Notice replies from \u20B93,999</p><p><a href="pricing.html">See Litigation plans</a></p></article></div></div></section>

<section class="sec tint"><div class="wrap">
<div class="head rv"><h2>Why clients choose Sancture</h2><p>Tax work is only as good as the process behind it. Ours is built around deadlines and evidence.</p></div>
<div class="grid">
<article class="card rv"><div class="ico">1</div><h3>Reviewed by professionals</h3><p>Every GST and Income Tax Return is checked by a qualified reviewer before it is filed.</p></article>
<article class="card rv"><div class="ico">2</div><h3>Deadline tracking</h3><p>We track due dates for each client and remind you early, which helps avoid late fees and interest.</p></article>
<article class="card rv"><div class="ico">3</div><h3>Ready for notices</h3><p>Clean records make notices easier to answer. If one arrives, the same team handles the reply.</p></article>
<article class="card rv"><div class="ico">4</div><h3>Published pricing</h3><p>Know the fee before you begin, with plans for individuals, businesses and disputes.</p></article></div></div></section>

<section class="sec"><div class="wrap split">
<div class="rv"><h2>Common questions about GST and ITR filing</h2><p style="margin-top:14px;color:var(--mute)">Short answers to what new clients ask us most. Need something specific? <a href="contact.html">Ask our team</a>.</p></div>
<div class="rv">
<details><summary>Who needs to file GST Returns?</summary><p>Businesses registered under GST file periodic returns such as GSTR-1 and GSTR-3B, including Nil Returns in months with no activity.</p></details>
<details><summary>What happens if I miss a filing deadline?</summary><p>Late fees and interest may apply, and prolonged non-filing can lead to further action such as cancellation of GST registration. Filing late is usually better than not filing.</p></details>
<details><summary>Can you reply to a GST or Income Tax notice?</summary><p>Yes. We review the notice, prepare the reply with supporting documents and represent you where required.</p></details>
<details><summary>Which documents do I need to start?</summary><p>For GST: sales and purchase invoices and your GST portal access. For ITR: PAN, Form 16 or income details, AIS/26AS and investment proofs.</p></details></div></div></section>

<section class="sec tint"><div class="wrap">
<div class="head rv"><h2>Fresh from our blog</h2></div>
<div class="grid">
<article class="card rv"><h3>GSTR-1 vs GSTR-3B: what is the difference?</h3><p>Understand what each return reports and why both must match.</p><p><a href="blogs.html">Read more</a></p></article>
<article class="card rv"><h3>Old vs new tax regime: how to choose</h3><p>A simple way to compare both regimes using your own numbers.</p><p><a href="blogs.html">Read more</a></p></article>
<article class="card rv"><h3>Got a GST notice? Start here</h3><p>The first steps to take before you reply.</p><p><a href="blogs.html">Read more</a></p></article></div></div></section>

<section class="sec navy"><div class="wrap" style="text-align:center"><h2 style="color:#fff;margin-inline:auto;max-width:18ch">Ready to put your tax filing on autopilot?</h2>
<p style="margin:18px auto 30px;color:#c3d3ea">Book a free consultation and we will suggest the right plan for you.</p><a class="btn light" href="contact.html">Book a consultation</a></div></section>
'''+FOOT+'<script src="js/flow.js"></script></body></html>'
w("index.html",home)

# ---------- SERVICES ----------
def svc(i,t,d,items,faq):
    return f'''<section class="svc" id="{i}"><div class="rv"><h2>{t}</h2><p style="margin-top:14px;color:var(--mute)">{d}</p><p style="margin-top:20px"><a class="btn" href="contact.html">Talk to an expert</a></p></div>
<div class="rv"><h3>What is included</h3><ul>{"".join("<li>%s</li>"%x for x in items)}</ul>
<details style="margin-top:20px"><summary>{faq[0]}</summary><p>{faq[1]}</p></details></div></section>'''
s=head("services.html","GST & Income Tax Services | Return Filing, Notices and Litigation | Sancture","Explore Sancture's GST return filing, income tax return filing, GST litigation and income tax litigation services, delivered with a clear process and published pricing.")
s+='''<section class="page-hero"><div class="wrap"><h1>Services built around your filing calendar</h1><p>From monthly GST returns to appeals before tax authorities, one team handles the work end to end.</p></div></section>
<div class="sec" style="padding-top:20px"><div class="wrap">'''
s+=svc("gst-returns","GST return filing","Stay compliant every month without chasing invoices or deadlines.",["Monthly and quarterly GSTR-1 and GSTR-3B filing","GSTR-2B reconciliation and input tax credit review","Annual return (GSTR-9) and reconciliation support","New GST registration and amendments","Filing reminders before every due date"],("What do you need from me each month?","Your sales invoices, purchase bills and any credit or debit notes. We tell you early if anything is missing."))
s+=svc("itr","Income tax return filing","Accurate returns for salaried individuals, professionals, businesses and investors.",["Salaried and pensioner returns with regime comparison","Business and professional income with books or presumptive taxation","Capital gains on shares, mutual funds and property","Advance tax computation and planning","Response to intimation notices after filing"],("Which ITR form applies to me?","It depends on your income sources, such as salary, business, capital gains or foreign assets. We select the right form after reviewing your documents."))
s+=svc("gst-litigation","GST litigation","Notices, assessments, appeals and registration matters handled by one team.",["Show cause notice analysis and reply drafting","Personal hearing representation before the proper officer","Appeals and related submissions","Cancellation and revocation of GST registration","Refund claims and rejections"],("I received a GST notice. What should I do first?","Do not ignore it. Note the reply deadline, collect the documents it refers to and share it with us so we can plan your reply."))
s+=svc("it-litigation","Income tax litigation","Defend your position in scrutiny, rectification, penalty and appeal proceedings.",["Reply to notices under the Income-tax Act","Scrutiny assessment support and hearings","Rectification and condonation applications","Appeals before the first appellate authority","Penalty and prosecution-related advisory"],("Can you help if I already filed my return late or incorrectly?","Often yes. Depending on the facts we can file a revised or updated return, or respond to any resulting notice."))
s+='''</div></div>
<section class="sec tint"><div class="wrap"><div class="head rv"><h2>How every engagement works</h2></div>
<div class="grid"><article class="card rv"><div class="ico">1</div><h3>Share documents</h3><p>Upload or send invoices, statements and notices securely.</p></article>
<article class="card rv"><div class="ico">2</div><h3>Verify and reconcile</h3><p>We check data against portal records and flag mismatches.</p></article>
<article class="card rv"><div class="ico">3</div><h3>Review and file</h3><p>A reviewer approves, you confirm, and we file on time.</p></article>
<article class="card rv"><div class="ico">4</div><h3>Acknowledge and follow up</h3><p>You get the acknowledgment and support for any follow-up.</p></article></div></div></section>'''+FOOT+'</body></html>'
w("services.html",s)

# ---------- PRICING ----------
p=head("pricing.html","Pricing | GST Return Filing, ITR Filing and Litigation Fees | Sancture","Transparent pricing for GST return filing, income tax return filing and notice or appeal support. Compare plans and request a custom quote from Sancture.")
p+='''<section class="page-hero"><div class="wrap"><h1>Pricing you can read in one minute</h1><p>Pick a service, compare plans and start. Prices are fixed for the scope listed.</p></div></section>
<section class="sec" style="padding-top:30px"><div class="wrap">
<div class="tabs" role="tablist"><button data-t="gst" role="tab" aria-selected="true">GST Returns</button><button data-t="it" role="tab" aria-selected="false">Income Tax Returns</button><button data-t="lit" role="tab" aria-selected="false">Litigation</button></div>
<div class="bill" id="bill"><span>Monthly</span><button class="sw" role="switch" aria-checked="false" aria-label="Bill yearly"></button><span>Yearly (2 months free)</span></div>
<p class="fine" id="note" style="margin-bottom:30px"></p>
<div class="plans" id="plans" aria-live="polite"></div></div></section>
<section class="sec tint"><div class="wrap split"><div class="rv"><h2>Pricing questions</h2></div><div class="rv">
<details><summary>Are there any hidden charges?</summary><p>No. Government fees and late fees, if any, are charged at actuals and always shared with you in advance.</p></details>
<details><summary>What counts as one invoice in the GST plans?</summary><p>Each sales or purchase invoice reported in the month. Credit and debit notes are counted with them.</p></details>
<details><summary>Can I switch plans later?</summary><p>Yes. You can move up or down at the start of any billing month.</p></details>
<details><summary>How do I pay?</summary><p>By UPI or bank transfer. A GST invoice is issued for every payment.</p></details></div></div></section>'''+FOOT+'</body></html>'
w("pricing.html",p)

# ---------- BLOGS ----------
posts=[("gst","GST","GSTR-1 vs GSTR-3B: what is the difference?","GSTR-1 reports your outward supplies, while GSTR-3B is the summary return where tax is paid. The two should reconcile, since mismatches are a common reason for notices."),
("gst","GST","Why you should reconcile GSTR-2B every month","GSTR-2B shows the input tax credit available to you. Comparing it with your purchase records each month helps you claim only what is eligible and spot supplier defaults early."),
("it","Income Tax","Old vs new tax regime: how to choose","Compare your total tax under both regimes using your actual deductions. If your eligible deductions are low, the new regime is often simpler; if they are high, the old regime may save more."),
("it","Income Tax","Received an income tax notice? First five steps","Read the notice fully, note the section and deadline, download the related documents from the portal, compare them with your records and then draft a reply that addresses each point."),
("lit","Litigation","Got a GST notice? Start here","Do not ignore it. Check the type of notice, the reply date and the period it covers. Gather supporting invoices and returns, then respond in writing and attend any hearing."),
("gst","GST","Input tax credit: common reasons it gets blocked","Typical causes include supplier non-filing, mismatches between invoices and GSTR-2B, and claims on items where credit is restricted. Regular reconciliation prevents most of them.")]
b=head("blogs.html","Tax Blog | GST and Income Tax Guides and Updates | Sancture","Plain-language guides on GST returns, income tax filing, notices and litigation from the Sancture team.")
b+='''<section class="page-hero"><div class="wrap"><h1>Tax guides in plain language</h1><p>Practical explainers on GST, income tax and notices from the Sancture team.</p></div></section>
<section class="sec" style="padding-top:30px"><div class="wrap"><div class="filters"><button data-c="all" aria-pressed="true">All</button><button data-c="gst" aria-pressed="false">GST</button><button data-c="it" aria-pressed="false">Income Tax</button><button data-c="lit" aria-pressed="false">Litigation</button></div><div class="grid">'''
for c,tag,t,x in posts:
    b+=f'<article class="card post" data-c="{c}"><span class="tag">{tag}</span><h3>{t}</h3><details><summary>Read article</summary><p>{x}</p><p style="margin-top:10px"><a href="contact.html">Ask us about your case</a></p></details></article>'
b+='</div></div></section>'+FOOT+'</body></html>'
w("blogs.html",b)

# ---------- CONTACT ----------
c=head("contact.html","Contact Sancture | Book a GST or Income Tax Consultation","Contact Sancture for GST return filing, income tax filing, notices and litigation support. Send an enquiry or book a consultation.")
c+=f'''<section class="page-hero"><div class="wrap"><h1>Tell us what you need filed or defended</h1><p>Send a short note and a consultant will reply within one business day.</p></div></section>
<section class="sec" style="padding-top:30px"><div class="wrap split" style="align-items:start">
<form id="enquiry" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
<div class="two"><label>Name<input name="name" required autocomplete="name"></label><label>Phone<input name="phone" type="tel" required autocomplete="tel"></label></div>
<label>Email<input name="email" type="email" required autocomplete="email"></label>
<label>I need help with<select name="topic" id="topic"><option>GST return filing</option><option>Income tax return filing</option><option>GST notice or litigation</option><option>Income tax notice or litigation</option><option>Nil Return</option><option>Starter</option><option>Growth</option><option>Elite</option><option>Annual Return</option><option>Book Keeping</option><option>Enterprise</option><option>Salaried</option><option>Business and Professional</option><option>Capital Gains and NRI</option><option>Notice Reply</option><option>Appeal and Hearing</option><option>Litigation Retainer</option></select></label>
<label>Message<textarea name="message" id="msg" rows="5"></textarea></label>
<button class="btn" type="submit">Send enquiry</button></form>
<div class="info rv"><div><b>Email</b><a href="mailto:{EMAIL}">{EMAIL}</a></div><div><b>Phone and WhatsApp</b><a href="tel:{PHONE.replace(' ','')}">{PHONE}</a></div><div><b>Office</b>Add your office address here</div><div><b>Hours</b>Monday to Saturday, 10 am to 6 pm</div></div>
</div></section>'''+FOOT+'</body></html>'
w("contact.html",c)

w("sitemap.xml",'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>{D}/{'' if h=='index.html' else h}</loc></url>" for h,_ in NAV)+"</urlset>")
w("robots.txt",f"User-agent: *\nAllow: /\nSitemap: {D}/sitemap.xml\n")
w("CNAME","www.sancture.in\n")
w("README.md","""# Sancture website

Static site for GitHub Pages. No build step needed (build.py only regenerates the HTML).

## Before going live
1. Replace the domain `www.sancture.in` in `CNAME`, `build.py` (D), sitemap.xml and robots.txt, then run `python3 build.py`.
2. Replace placeholder email, phone, WhatsApp number and office address in `build.py`.
3. Create a free form at formspree.io and put its ID in `contact.html` (YOUR_FORM_ID).
4. Replace `assets/logo.png` with a higher resolution logo if you have one.

## Deploy
1. Push this folder to a GitHub repository.
2. Settings > Pages > Deploy from branch (main, root).
3. Add a CNAME DNS record for `www` pointing to `<username>.github.io`, and A records for the apex domain to GitHub Pages IPs (see GitHub docs).
4. Tick Enforce HTTPS.
""")
