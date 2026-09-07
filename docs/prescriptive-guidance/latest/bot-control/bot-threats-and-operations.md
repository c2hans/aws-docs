---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/bot-control/bot-threats-and-operations.html
---

# Understanding bot threats and operations
<a name="bot-threats-and-operations"></a>

According to [Security Today](https://securitytoday.com/articles/2023/05/17/report-47-percent-of-internet-traffic-is-from-bots.aspx), more than 47% of all traffic on the internet is due to bots. This includes the helpful portion of bots, those that self-identify and provide value. About 30% of bot traffic is unidentified bots that are performing malicious activities, such as DDoS attacks, ticket scalping, inventory scraping, or hoarding. [Security Magazine](https://www.securitymagazine.com/articles/99823-there-was-a-387-increase-in-attack-activity-from-q1-to-q2-2023) reports a 300% increase in volumetric DDoS events during the first half of 2023. This makes this topic more relevant, and it makes knowledge about the available preventative and protective tools and technology all the more important.

The following table categorizes the different types of bot activity and the business impact each one can have. This is not meant to be an extensive list; it is a summary of the most common bot activities. It highlight the importance of monitoring and mitigation controls. For an extensive list of bot threats, visit the [OWASP Automated threats to applications handbook](https://owasp.org/www-project-automated-threats-to-web-applications/) (OWASP website).

|
|
| Bot activity type | Description | Potential impact |
| --- |--- |--- |
| Content scraping | Copying of proprietary content for use by third-party sites | Impact to your SEO due to content duplication, brand impact, and performance problems caused by aggressive scrapers |
| Credential stuffing | Testing of stolen credential databases in your website to obtain access or validate information | Problems for users, such as fraud and account lockouts, which increase support queries and decrease brand trust |
| Card cracking | Testing databases of stolen credit card data to validate or complement missing information | Problems for users, such as identity theft and fraud, and damage to your fraud score |
| Denial of service | Increasing traffic to a specific website to slow down response or make it unavailable for legitimate traffic | Loss of revenue and damage to reputation |
| Account creation | Creation of multiple accounts with the purpose of misuse or financial gain | Hindered growth and skewed marketing analytics |
| Scalping | Obtaining limited availability goods, frequently tickets, over genuine consumers | Loss of revenue and problems for users, such as lack of access to goods being sold |

## How botnets operate
<a name="botnets"></a>

The tactics, techniques, and procedures (TTP) of botnet operators have evolved substantially over time. They have had to keep up with the detection and mitigation technologies developed by companies. The following figure shows this evolution. Botnets started simply by using IP addresses as a means of operation, and they eventually evolved to use sophisticated, human biometric emulation. This sophistication is expensive, and not all botnets use the most advanced tools. There are a mix of operators in the internet, and they likely evaluate the best tool for the job to provide a good return on investment. One goal in bot defense is to make the botnet activity expensive so that the target is no longer viable.

![Evolution in bot tactics, techniques, and procedures](https://docs.aws.amazon.com/prescriptive-guidance/latest/bot-control/images/guide-img/7c615558-ea52-4b14-ae3f-0e853a88c41f/images/13b1f3b1-1685-4594-af78-00fcfec54f35.png)

Generally, bots are categorized as common or targeted:
+ **Common bots** – These bots self-identify and won't attempt to emulate browsers. Many of these bots perform useful tasks, such as content crawling, search engine optimization (SEO), or aggregation. It's important to identify and understand which of these common bots come to your site and the effect they have on your traffic and performance.
+ **Targeted bots** – These bots try to evade detection by emulating browsers. They use browser technology, such as headless browsers, or they fake browser fingerprints. They have the ability to execute JavaScript and support cookies. Their intent is not always clear, and the traffic they generate can look like normal user traffic.

The most advanced and persistent targeted bots emulate human behavior by generating human-like mouse movements and clicks on a website. They are the most sophisticated and difficult to detect, but they are also the most expensive to operate.

Often, an operator combines these techniques. This creates a game of constant pursuit, where you have to frequently change the protection and mitigation approach in order to adapt to the operator's latest techniques. These bots are considered to be an *advanced persistent threat (APT)*. For more information, see [Advanced persistent threat](https://csrc.nist.gov/glossary/term/advanced_persistent_threat) in the NIST resource center.
