# -*- coding: utf-8 -*-
# All site content. Text follows Shiloh's approved wording.

EMAIL = "shilohayala@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/shilohayala/"
GITHUB = "https://github.com/shilohayala"
CV = "assets/Shiloh_Ayala_CV.pdf"

TAGLINE_LONG = "Data analysis in mental healthcare · MSc Health Innovation &amp; Data Science · emlyon business school"
TAGLINE_SHORT = "Data analysis in mental healthcare · MSc, emlyon"

BIO_LONG = ("I’m learning to use data to improve mental health access and outcomes. My Psychology studies, with a focus on "
            "systems science, and my experience in evidence-based complementary care showed me how infrastructure, cost, "
            "stigma, and fragmented care networks keep people from the care they need. I’m now building my data analytics "
            "skills to help design mental health programs and interventions that address disparities in care, and I’d love "
            "to connect with anyone working toward systemic, patient-centered change in mental healthcare.")
BIO_SHORT = ("I’m learning to use data to improve mental health access and outcomes. My Psychology studies, focused on systems "
             "science, and my work in complementary care showed me how cost, stigma and fragmented care keep people from help, "
             "and I’m building my analytics skills to change that.")

def li(name, url):
    return f'<a href="{url}">{name}</a>'

# ---------------------------------------------------------------- PROJECTS (newest first)
PROJECTS = [
 dict(slug="ess-wellbeing-france",
  title="In France, peri-urban residents report the highest wellbeing, not city dwellers",
  meta="Jun 2026 · Self-directed", date="Jun 2026", context="Self-directed",
  thumb="ess-thumb.jpg", thumb_pos="0% 50%",
  thumb_alt="Where do French residents report the highest wellbeing? European Social Survey 2002 to 2023, 20,809 French respondents",
  desc="Queried 20 years of European Social Survey data (20,809 French respondents) in SQL to compare wellbeing across residential areas.",
  tags=["SQL", "SQLite", "ESS"],
  cover=None,
  body="""
<p>Living in Lyon for just under a year, I’ve benefited from what European cities are famous for in the U.S., namely, the walkability and quality public transit. Simultaneously, I’ve spent enough time on trams to the suburbs to notice where the system stops working, and I find myself repeatedly frustrated by infrastructure gaps that fail the system’s users and feel entirely fixable.</p>
<p>In 2024, I <a href="../writing/mental-health-infrastructure.html">wrote about</a> the relationship between land use, infrastructure, and mental health outcomes, arguing that we improve wellbeing faster by fixing high-leverage environmental factors than by scaling individual interventions alone. I wanted to bring some data to that instinct. For this SQL project, I cleaned and queried the European Social Survey (2002-2023), 530,711 respondents across Europe, filtering to 20,809 French responses.</p>
<p>I initially planned to use a transport satisfaction variable but found it had less than 10% coverage for French respondents (2,010 of 20,809) and pivoted to the residential area variable instead, excluding refusals and non-responses from the wellbeing variables before running any averages. This is an imperfect substitution, because where someone lives is not the same as the quality of the transport they rely on, so it can point to patterns worth investigating rather than answer questions about infrastructure directly. The wider literature gives reason to keep looking. Conceição et al. (2023)<sup><a href="#ref-1" id="cite-1">1</a></sup>, the review behind my earlier reflection, synthesised 69 empirical studies and found evidence linking transport infrastructure, congestion and delays to negative affective states and psychological distress. The happiness and life satisfaction measures I used are subjective wellbeing scales, not clinical instruments, and I’m treating them as such.</p>
<figure><img src="../assets/ess-sql.jpg" alt="The main SQL query, averaging happiness and life satisfaction by residential area for French respondents, with its results" loading="lazy"><figcaption>The main query and its results</figcaption></figure>
<p>The results didn’t go where I expected after reading that review. Residents of suburbs and the outskirts of big cities reported the highest average happiness (7.33 out of 10, n = 2,560) and life satisfaction (6.64) of any residential category, followed closely by country villages and rural homes. Town and small city residents scored lowest on both (7.14 and 6.36, n = 6,857), not big city residents. The oft-assumed gradient of urban is better and suburban is worse doesn’t show up here, and suburbs stay on top and towns at the bottom whether I look at the early survey rounds (2002-2008) or the recent ones (2018-2023), so pooling twenty years of data isn’t what produces the pattern.</p>
<div class="table-wrap"><table>
<caption>Average self-reported wellbeing by residential area, French respondents, ESS 2002–2023, unweighted, 0 to 10 scales</caption>
<thead><tr><th>Residential area</th><th class="num">n</th><th class="num">Happiness</th><th class="num">Life satisfaction</th></tr></thead>
<tbody>
<tr class="top"><td>Suburbs or outskirts of big city</td><td class="num">2,560</td><td class="num">7.33</td><td class="num">6.64</td></tr>
<tr><td>Country village</td><td class="num">6,209</td><td class="num">7.29</td><td class="num">6.51</td></tr>
<tr><td>Farm or home in countryside</td><td class="num">1,287</td><td class="num">7.21</td><td class="num">6.58</td></tr>
<tr><td>Big city</td><td class="num">3,797</td><td class="num">7.18</td><td class="num">6.43</td></tr>
<tr><td>Town or small city</td><td class="num">6,857</td><td class="num">7.14</td><td class="num">6.36</td></tr>
</tbody></table></div>
<p>The differences are modest, the figures are unweighted, and confirming them would take proper statistical testing, which is my next step.</p>
<p>That caveat raises its own question in my eyes. If the people most affected by infrastructure inequality are reporting reasonable wellbeing on large population surveys, does that make it easier for policymakers to deprioritize them and go on with business as usual? How can we, the community of health innovators and developers, better center these communities and advocate for them in our work?</p>
""",
  tools="SQL, DB Browser for SQLite",
  links=[("View the code on GitHub", "https://github.com/shilohayala/ESS-wellbeing-by-urban-environment")],
  sources=[
   'Conceição, M. A. et al. (2023). The effect of transport infrastructure, congestion and reliability on mental wellbeing: a systematic review of empirical studies. <em>Transport Reviews</em>, 43(2), 264–302. <a href="https://doi.org/10.1080/01441647.2022.2100943">doi.org/10.1080/01441647.2022.2100943</a>',
  ],
  data_note='Data: <a href="https://www.europeansocialsurvey.org/data-portal">European Social Survey</a>, rounds 1–11.',
 ),
 dict(slug="brfss-childhood-exposure",
  title="Alcohol is the most visible childhood exposure in CDC survey data",
  meta="Jun 2026 · Self-directed", date="Jun 2026", context="Self-directed",
  thumb="brfss-thumb.jpg", thumb_pos="50% 50%",
  thumb_alt="Bar chart of adverse childhood experiences: alcohol use disorder in the home 23.5%, mental illness 17.9%, illegal drug use 9.3%",
  desc="Cleaned and queried the CDC’s 2021 BRFSS survey (438,693 responses) in SQL to look at adverse childhood experiences, depression and drinking.",
  tags=["SQL", "SQLite", "CDC BRFSS"],
  cover=None,
  body="""
<p>The <a href="https://www.linkedin.com/company/cmsmodelwhosociety/">CMS Model WHO Society</a> event in Lisbon, a simulation of the World Health Assembly, was centered on Reframing the Global Response to Substance Use.</p>
<p>Researching this opportunity while teaching myself SQL got me wondering how I could tie the two together. For my first SQL project, I cleaned and queried the CDC’s 2021 Behavioral Risk Factor Surveillance System, consisting of 438,693 survey responses across 303 columns. I recoded survey-specific placeholder values, converted alcohol frequency responses from a mixed weekly/monthly format into comparable units, and determined which non-responses reflected genuine missing data versus optional survey modules.</p>
<figure><img src="../assets/brfss-sql.jpg" alt="SQL query counting adverse childhood experiences in the BRFSS data, with its results" loading="lazy"><figcaption>SQL Project Series, Week One</figcaption></figure>
<p>Exploring this data as a SQL newbie proved fruitful for turning these health challenges over in my mind.</p>
<p>Among respondents asked about adverse childhood experiences, recalled exposure to alcohol use disorder in the home (23.5%) was more than twice the rate of recalled illegal drug use (9.3%), with mental illness sitting in between at 17.9%. Alcohol was clearly the most visible. From my vantage point, that gap likely reflects stigma and recognition more than true prevalence, and has real implications for which harms get addressed and which stay hidden. It’s worth noting at the same time that this module was optional across states, so these figures represent participating respondents rather than the full US population.</p>
<figure><img src="../assets/brfss-infographic.jpg" alt="Infographic: among 56,655 respondents asked about adverse childhood experiences, 23.5% recalled alcohol use disorder in the home, 17.9% mental illness or depression, 9.3% illegal drug use. Average drinking days per month: 4.5 with a depression diagnosis, 5.0 without" loading="lazy"><figcaption>Graphic by Shiloh Ayala</figcaption></figure>
<p>The next observation surprised me. Adults with a diagnosed depressive disorder averaged 4.5 drinking days per month, compared to 5.0 for those without one. These averages include non-drinkers, counted as zero drinking days. The difference is modest enough to warrant further statistical testing, but the direction was counterintuitive regardless.</p>
<p>There are two explanations I think could reflect sides of the same coin. Diagnosis ties people into the care system, which could potentially reduce harmful drinking. Or those without a diagnosis may be managing undiagnosed symptoms with alcohol, a well-documented pattern in the literature. Either way, what gets identified gets addressed, which matters enormously in the massive number of cases where substance abuse and mental health challenges overlap.</p>
<p>A limitation worth naming is that this survey doesn’t differentiate between types of substance use, which shapes what questions I can and can’t ask of the data. This mirrors a broader issue in how drug use gets discussed as a monolith, impacting how patient-centered we can be in our design of truly effective treatment pathways.</p>
<p>To tie things up, I cross-checked my findings against the CDC’s published codebook figures to verify nothing got distorted in the cleaning process. All figures here are unweighted sample proportions, so applying the BRFSS survey weights is a natural next step. And a note that this data is from 2021, a COVID-era snapshot, so mental health indicators were likely elevated relative to pre-pandemic norms.</p>
""",
  tools="SQL, DB Browser for SQLite",
  links=[("View the code on GitHub", "https://github.com/shilohayala/brfss-2021-ace-analysis")],
  sources=[],
  data_note='Data: <a href="https://www.cdc.gov/brfss/annual_data/annual_2021.html">CDC Behavioral Risk Factor Surveillance System, 2021</a>.',
 ),
 dict(slug="oraiti",
  title="orAIti, AI triage for patients who don’t know when to seek care",
  meta="Apr 2026 · HSIL Hackathon", date="Apr 2026", context="Harvard HSIL Hackathon · Coup de Coeur award",
  thumb="oraiti-title.jpg", thumb_pos="50% 50%",
  thumb_alt="orAIti, AI health companion, title slide with the team names",
  desc="Team project that won the Coup de Coeur award. I worked on competitor and patient research, the value proposition and partner strategy.",
  tags=["Market research", "Value proposition", "Business model"],
  cover=("oraiti-title.jpg", "orAIti, AI health companion, title slide with the team names", None),
  body="""
<p>In April 2026, my team and I took part in the Harvard Health Systems Innovation Lab’s annual worldwide hackathon, where over two days we developed orAIti, a patient-facing LLM-driven triage tool and business model with bidirectional benefits. It equips patients to start their care journeys with confidence while reducing unnecessary ER utilization, and it would be accessible through well-matched NGO partners, providers, and insurers, giving their users a more reliable triage tool than commonly-relied-upon alternatives. Our project won the Coup de Coeur award.</p>
<h2>Who gets lost in the system</h2>
<p>Patients with low health literacy face a three-part breakdown. They can’t assess what their symptoms mean, they don’t know who to contact or when, and they can’t advocate for urgency when they do. That drives two costly failures, delayed care for serious conditions and emergency departments filled with patients who needed a GP rather than a hospital. France recorded around 21.3 million emergency department visits in 2024<sup><a href="#ref-1" id="cite-1">1</a></sup>, regional health agency estimates suggest 30 to 40% of those patients could have been cared for elsewhere<sup><a href="#ref-2" id="cite-2">2</a></sup>, and each visit costs the public system about €227<sup><a href="#ref-3" id="cite-3">3</a></sup>.</p>
<h2>How it works</h2>
<p>A fine-tuned LLM handles intake, letting the patient describe what’s happening in their own words and mapping it to structured clinical data, with follow-up questions grounded in what clinicians actually ask. A rule-based triage layer then judges how serious it is, either telling the patient to go now and why, or explaining what to watch for and when to escalate. Finally, an LLM drawing on validated sources builds an action plan covering what to do now, what to say to their doctor, and how to advocate for themselves if they’re dismissed.</p>
{{VIDEO:oraiti}}
<h2>Where I came in</h2>
<p>Everything in this project was a genuine team effort, and the ideas grew out of conversations we all shared. Within that, I contributed to identifying the weaknesses of our competitors, the free general-purpose LLMs many people already turn to with health questions, and the concerns patients have when using them, along with who feels those pains most, parents being one clear example. I helped shape how we positioned orAIti as a patient education tool that also brings major financial and operational benefits to hospitals and insurers, which became the heart of our value proposition, and I helped identify potential partners and investors who might be interested. Caitlin Chesnais-Dixon and I brainstormed the revenue model together, where we decided on the insurance and NGO channels. orAIti would be funded through NGO grants and paid licences for insurers, employers and hospital networks.</p>
<h2>Two days, many pivots</h2>
<p>My first hackathon was an exciting trial-by-fire in understanding how product development happens in this space. With each round of mentor feedback, our project evolved and pivoted rapidly. Keeping the patient experience at the core, especially for those with lower health literacy, proved challenging while balancing all the considerations that go into generating viable health tools. We succeeded in centering patient needs in our value proposition, which led us to win the Coup de Coeur award.</p>
<p class="credits">Built with <a href="https://www.linkedin.com/in/antoine-chesnais-311b69ab/">Antoine Chesnais</a>, <a href="https://www.linkedin.com/in/caitlin-chesnais-dixon-358984186/">Caitlin Chesnais-Dixon</a>, <a href="https://www.linkedin.com/in/lorena-g%C3%B3mez-acosta-1b996525a/">Lorena Gómez Acosta</a> and <a href="https://www.linkedin.com/in/m%C3%A9lissa-laine-5845b538b/">Mélissa Laine</a>, and with thanks to <a href="https://www.linkedin.com/in/sia-togarrati-0a1469126/">Sia Togarrati</a>, whose personal experience helped ground our understanding of what patients need.</p>
""",
  tools=None, links=[],
  related=('Related post', '../writing/harvard-hsil-hackathon.html', 'Hackathon at the Harvard Health Systems Innovation Lab'),
  sources=[
   'DREES (2026). <em>Les établissements de santé en 2024</em>, édition 2026. <a href="https://drees.solidarites-sante.gouv.fr/publications-communique-de-presse-documents-de-reference/panoramas-de-la-drees/260520-Etablissements-de-sant%C3%A9-en-2024">drees.solidarites-sante.gouv.fr</a>',
   'ARS Hauts-de-France estimate, as reported in “La France a dépensé des millions pour créer un numéro censé désengorger les urgences”, <em>Sciencepost</em>. <a href="https://sciencepost.fr/la-france-a-depense-des-millions-pour-creer-un-numero-cense-desengorger-les-urgences-trois-ans-apres-elles-affichent-25-de-passages">sciencepost.fr</a>',
   'French government, <em>En avoir pour mes impôts</em> (2023), as reported in “En avoir pour mes impôts : 227 euros le passage aux urgences”, <em>La Santé au Quotidien</em>. <a href="https://lasanteauquotidien.com/actualite-sante/en-avoir-pour-mes-impots-227-euros-le-passage-aux-urgences/">lasanteauquotidien.com</a>',
  ],
  data_note=None,
 ),
 dict(slug="ehpad-data-model",
  title="Designing the data model for an EHPAD dehydration risk tool",
  meta="Mar 2026 · emlyon, Project Management", date="Mar 2026", context="emlyon business school · Project Management",
  thumb="ehpad-title.jpg", thumb_pos="50% 50%",
  thumb_alt="Title slide, AI-Driven Dehydration Clinical Risk Scoring Interface for EHPAD, Lyon",
  desc="Built the data model for an AI tool that helps nurses at a Lyon care home spot residents most at risk of dehydration.",
  tags=["Data modelling", "UML", "Project management"],
  cover=("ehpad-title.jpg", "Title slide, AI-Driven Dehydration Clinical Risk Scoring Interface for EHPAD, Lyon", None),
  body="""
<p>In early 2026, seven of us in our Project Management course at emlyon built a full project dossier for EHPAD Korian Les Terrasses de Blandan, a care home in Lyon with 110 residents. Elderly residents are at higher risk of dehydration, especially during heatwaves, because of reduced thirst sensation, limited mobility and cognitive impairment, and Lyon’s summers aren’t getting any cooler. Most facilities still monitor hydration reactively, with the same manual checklist for every resident regardless of their individual risk. Our proposal was an AI-driven risk scoring interface that combines resident health data with weather forecasts to give nurses a daily prioritised list of who needs attention first, with nurses always able to override the AI’s call.</p>
<p>My main piece was the data model, the UML class diagram that maps what information the system needs and how it all fits together. I worked out which data the tool would draw on, from heart rate, sodium and creatinine levels in the patient health record to temperature, humidity and heatwave alerts in the forecast, and how each piece relates to the others. Patient data and weather data both feed into a central set of dehydration risk scores, which roll up into a daily priority list and connect to each nurse’s profile and assigned residents, so the interface can show every nurse who to see first.</p>
<figure><img src="../assets/ehpad-data-model.jpg" alt="UML class diagram linking weather data, patient health record and patient profile to dehydration risk scores, which feed a risk priority list, nurse profiles and the user interface" loading="lazy"><figcaption>The data model (UML class diagram)</figcaption></figure>
<p>I also helped write the slides framing the problem, contributed to a couple of iterations of our work breakdown structure, and presented the system design to the class, walking through both our use case diagram and the data model. Beyond that, I was in charge of visually streamlining and editing the whole slide deck, so that seven people’s work came together as one coherent presentation.</p>
<p>Looking back with a few more months of study behind me, there are two things I’d change. A single day’s forecast applies to every resident, so weather data should connect to risk scores as one-to-many rather than one-to-one, and the current risk score is stored in two places, which risks the two drifting out of sync.</p>
<p class="credits">Built with Caitlin Chesnais-Dixon, Xintian Huang, Mélissa Laine, Thomas Junior Nembot, Christabelle Nguessie Essofack Matsinkou and Océane Thouvard-Kwek.</p>
""",
  tools=None, links=[], sources=[], data_note=None,
 ),
]

# ---------------------------------------------------------------- POSTS (newest first)
POSTS = [
 dict(slug="lgbtqi-disclosure-france",
  title="Disclosure, concealment and LGBTQI mental health in France", date="Jul 2026",
  img="post-disclosure.jpg", img_alt="Ink illustration of a crowd of identical faces, with one person covering their mouth",
  credit="Art: Jennifer Hom",
  teaser="The Trevor Project’s 2025 survey on LGBTQI youth mental health sent me searching for what European data shows, particularly in France, where I live.",
  body="""
<p><a href="https://www.thetrevorproject.org/">The Trevor Project</a> recently released its 2025 survey results on LGBTQI youth mental health in the US. It sent me searching for what European data shows, particularly in France, where I live.</p>
<p>Something I keep coming back to in my health data studies is how many of the health outcomes we measure turn out to be downstream consequences of poor treatment within systems meant to help people.</p>
<p>This week I spent time in the <a href="https://fra.europa.eu/">European Union Agency for Fundamental Rights</a> LGBTI Survey data, looking at French respondents specifically. 41% reported feeling depressed or downhearted some of the time in the last two weeks. That figure sits differently when you look at it alongside the disclosure data: 46% of LGBTI people across the EU did not disclose their identity to any healthcare provider, and 66% said none or only a few of their health providers know they are LGBTI.</p>
<p>The workplace numbers tell a similar story about where people feel safe being known. 72% are not out to clients or customers, and 55% are not out to supervisors. That drops to 33% for colleagues, a gap that points to real concern about how disclosure affects relationships where power is unequal.</p>
<p>The hand-holding figure landed especially hard. A majority of LGBTI respondents in France said they avoid holding hands with a same-sex partner in public, with rates notably higher among gay and bisexual men than women.</p>
<p>Concealment is a chronic stressor with measurable mental health consequences. A 2020 meta-analysis across 193 studies found consistent associations between sexual orientation concealment and depression, anxiety, and psychological distress (Pachankis et al.). When concealment extends into healthcare settings, it creates specific barriers. Patients may withhold information that is directly relevant to care or avoid care altogether in contexts where their identity makes them feel unsafe. For the cases where identity is relevant to care, the consequences are clinical, not just social as is often assumed.</p>
<p>Both the BRFSS and ESS datasets I’ve been working with this summer either excluded sexual orientation variables entirely or lacked sufficient coverage to draw meaningful conclusions about LGBTQI populations. The absence of data is never neutral; it shapes who gets studied and whose health is treated as a policy priority.</p>
<p>For us working in healthcare, creating explicitly affirming spaces where patients have reason to believe disclosure is safe is a care quality decision that is entirely within reach.</p>
""",
  sources=[
   'European Union Agency for Fundamental Rights, <em>LGBTI Survey II</em>, FRA Data Explorer. <a href="https://fra.europa.eu/">fra.europa.eu</a>',
   'Pachankis, J. E., Mahon, C. P., Jackson, S. D., Fetzner, B. K. &amp; Bränström, R. (2020). Sexual orientation concealment and mental health: A conceptual and meta-analytic review. <em>Psychological Bulletin</em>, 146(10), 831–871. <a href="https://doi.org/10.1037/bul0000271">doi.org/10.1037/bul0000271</a>',
  ],
  related=None,
 ),
 dict(slug="harvard-hsil-hackathon",
  title="Hackathon at the Harvard Health Systems Innovation Lab", date="Apr 2026",
  img="oraiti-title.jpg", img_alt="orAIti, AI health companion, title slide with the team names", credit=None,
  teaser="Over two days, my team developed a patient-facing LLM-driven triage tool and business model with bidirectional benefits.",
  body="""
<p>This April I had the opportunity to put my coursework to the test at the <a href="https://www.linkedin.com/company/harvardhsi/">Harvard Health Systems Innovation Lab</a>’s annual worldwide hackathon.</p>
<p>Over two days, my team developed orAIti, a patient-facing LLM-driven triage tool, along with a business model with bidirectional benefits. It would equip patients to start their care journeys with confidence while reducing unnecessary ER utilization. Our model would be accessible through well-matched NGO partners, providers, and insurers, giving their users a more reliable triage tool than commonly-relied-upon alternatives.</p>
<p>My first hackathon was an exciting trial-by-fire in understanding how product development happens in this space. With each round of mentor feedback, our project evolved and pivoted rapidly. Keeping the patient experience at the core, especially for those with lower health literacy, proved challenging while balancing all the considerations that go into generating viable health tools. We succeeded in centering patient needs in our value proposition, which led us to win the Coup de Coeur award.</p>
<p>Thank you to <a href="https://www.linkedin.com/in/antoine-chesnais-311b69ab/">Antoine Chesnais</a> for bringing your expertise in model architecture, prototype-building, and patient-centered drive, to <a href="https://www.linkedin.com/in/lorena-g%C3%B3mez-acosta-1b996525a/">Lorena Gómez Acosta</a> and <a href="https://www.linkedin.com/in/m%C3%A9lissa-laine-5845b538b/">Mélissa Laine</a> for your market research, prototype collaboration, and pitch-building excellence, and to <a href="https://www.linkedin.com/in/caitlin-chesnais-dixon-358984186/">Caitlin Chesnais-Dixon</a> for your wealth of industry and model-building knowledge, the most legendary business-model brainstorming session, and for cultivating the creative seed for this entire opportunity.</p>
<p>And thanks to the organizers, judges, and all the excellent mentors who helped us carve our project along the way.</p>
""",
  sources=[],
  related=('Related project', '../work/oraiti.html', 'orAIti, AI triage for patients who don’t know when to seek care'),
 ),
 dict(slug="trust-ai-mental-healthcare",
  title="What it takes to trust AI in mental healthcare", date="Mar 2026",
  img="post-ai-sphere.jpg", img_alt="Abstract glowing sphere of iridescent colour on a dark background",
  credit="Image: mmnvaldez via Pinterest",
  teaser="I will always advocate for a world where everyone receives truly personalized, continuous mental healthcare.",
  body="""
<p>I recently watched Forbes’ interview on how Spring Health is setting the standard for AI in mental health, and it has stayed on my mind since. I will always advocate for a world where everyone receives truly personalized, continuous mental healthcare. At the same time, we’re facing massive provider shortages and access barriers that impact our most vulnerable community members, and those gaps are not going to close on their own any time soon.</p>
{{VIDEO:forbes}}
<p>While AI steps in to help fill these gaps and support providers, we need to be honest about the stakes. When it comes to mental health, we are working with people’s most vulnerable moments, in life and in health. A tool that misses a sign of risk or responds without care is not a small technical error, because it can shape whether someone decides to reach out for help again.</p>
<p>This interview, especially the introduction of <a href="https://www.springhealth.com/blog/introducing-vera-mh-new-standard-ethical-ai-mental-healthcare">VERA-MH</a>, spotlights the possibility of rigorous and scalable tools for measuring safety outcomes. VERA-MH, which stands for Validation of Ethical and Responsible AI in Mental Health, is an evaluation framework that Spring Health built together with practicing clinicians, suicide prevention experts, ethicists and AI developers. It looks at whether mental health chatbots can recognize risk, respond with empathy and know when to bring a human into the conversation. I was glad to see it released as an open-source evaluation, so that others in the field can use it, test it and push it further.</p>
<p>Patients can’t afford for ethics to be an afterthought, and this interview centers the need for transparency about what these tools can and can’t do. I am impressed with Spring Health’s ability to match the scale of the issue to the quality of potential solutions, and I hope to see more organizations hold their tools to this kind of standard.</p>
""",
  sources=[
   'Spring Health, “Introducing VERA-MH: A new standard for ethical AI in mental healthcare”. <a href="https://www.springhealth.com/blog/introducing-vera-mh-new-standard-ethical-ai-mental-healthcare">springhealth.com</a>',
  ],
  related=None,
 ),
 dict(slug="at-home-oncology-care",
  title="One week on at-home oncology care, with Human Care and Sanofi", date="Oct 2025",
  img="post-oncology.jpg", img_alt="Shiloh presenting a slide on patient hesitancy to classmates at emlyon", credit=None,
  teaser="My colleagues at Emlyon and I collaborated to present a picture of at-home oncology treatment in Germany, with patients at the core of our strategy.",
  body="""
<p>In one week, my colleagues at Emlyon and I collaborated to present a picture of at-home oncology treatment in Germany, and paths forward for implementing it, with patients at the core of our strategy.</p>
<p>The project was set by <a href="https://www.linkedin.com/in/axelle-ayad/">Axelle Ayad</a> at <a href="https://www.linkedin.com/company/humancare-group/">Human Care</a> and Romain Aubris at <a href="https://www.linkedin.com/company/sanofi/">Sanofi</a>, and the opportunity they gave us to practice this work in real time has been invaluable. It has been instrumental in discovering where I can grow, not only as a speaker, but as a time-bound project analyst. Current challenges in global health require timely implementation of new systems, and working within a single week gave me a real sense of what that asks of a team.</p>
<p>I look forward to building on what I’ve learned in projects to come at Emlyon, especially in mental health, where timeliness is of the essence.</p>
<p>Thank you to <a href="https://www.linkedin.com/in/m%C3%A9lissa-laine-5845b538b/">Mélissa Laine</a>, <a href="https://www.linkedin.com/in/sia-togarrati-0a1469126/">Sia Togarrati</a>, <a href="https://www.linkedin.com/in/mariana-andrade-ab3347296/">Mariana Andrade</a>, <a href="https://www.linkedin.com/in/am%C3%A8l-boualla-10aa32389/">Amèl Boualla</a>, <a href="https://www.linkedin.com/in/caitlin-chesnais-dixon-358984186/">Caitlin Chesnais-Dixon</a>, <a href="https://www.linkedin.com/in/lorena-g%C3%B3mez-acosta-1b996525a/">Lorena Gómez Acosta</a>, <a href="https://www.linkedin.com/in/beatrice-carlotta-meazza-a61339262/">Beatrice Carlotta Meazza</a>, <a href="https://www.linkedin.com/in/nicolezhuang/">Yunzhu Zhuang</a> and <a href="https://www.linkedin.com/in/valerie-cerna-reichmann-858275229/">Valerie Cerna Reichmann</a> for all your amazing energy and research through this project.</p>
""",
  sources=[], related=None,
 ),
 dict(slug="mental-health-infrastructure",
  title="Mental health is an infrastructure problem too", date="Aug 2024",
  img="post-infrastructure.jpg", img_alt="Urban planning map of a neighbourhood showing living, commercial and social zones connected by walking routes",
  credit="Image: ecemz0 via Pinterest",
  teaser="Human health is inseparable from safe, effective, and culturally responsive land use.",
  body="""
<p>Again, we find that human health is inseparable from safe, effective, and culturally responsive land use.</p>
<p>Below is a fascinating review of the mental health outcomes of poor transportation infrastructure, and the results should not surprise: well-designed and maintained transportation options greatly improve long-term wellbeing in our communities.</p>
<p>The colloquial answer to our mental health crisis is psychotherapy. While therapy has an indisputable place in mental health treatment, our therapists and their clients are burdened by a world overdue for systems-level changes. Human health has always been tied to the landscapes we navigate daily; if those landscapes are underfunded, unmaintained, and don’t serve their communities effectively, we see poor outcomes replicated over generations.</p>
<p>While it is easy to argue for a therapist per person, we can improve mental health outcomes faster by making changes in high-leverage areas of health, such as better infrastructure.</p>
""",
  sources=[
   'Conceição, M. A. et al. (2023). The effect of transport infrastructure, congestion and reliability on mental wellbeing: a systematic review of empirical studies. <em>Transport Reviews</em>, 43(2), 264–302. <a href="https://www.tandfonline.com/doi/full/10.1080/01441647.2022.2100943">tandfonline.com</a>',
  ],
  related=('Related project', '../work/ess-wellbeing-france.html', 'In France, peri-urban residents report the highest wellbeing, not city dwellers'),
 ),
]

VIDEOS = {
 "oraiti": dict(title="orAIti demo", by="Video: orAIti team", url="https://youtu.be/mPXtUrRwURw",
                embed="https://www.youtube-nocookie.com/embed/mPXtUrRwURw", site="YouTube"),
 "forbes": dict(title="How Spring Health Is Setting the Standard for AI in Mental Health", by="Video: Forbes",
                url="https://www.forbes.com/video/4f6e5757-dd18-4d50-8ee9-ba693e532fe5/how-spring-health-is-setting-the-standard-for-ai-in-mental-health/",
                embed=None, site="Forbes"),
}
