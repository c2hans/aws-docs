---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/bot-control/introduction.html
---

# Implementing a bot control strategy on AWS
<a name="introduction"></a>

*Diana Alvarado, Geary Scherer, Tzoori Tamam, and Cameron Worrell, Amazon Web Services*

The internet as we know it would not be possible without bots. *Bots* run automated tasks over the internet and simulate human activity or interaction. They allow businesses to build efficiency into processes and tasks. Useful bots, like web crawlers, index information on the internet and help us quickly find the most relevant information for our search queries. Bots are a good mechanism to improve business and provide value to companies. However, with time, bad actors started using bots as a means to abuse existing systems and applications in new and creative ways.

Botnets are the best-known mechanism to scale bots and their impact. *Botnets* are networks of bots that are infected by [malware](https://en.wikipedia.org/wiki/Malware) and are under the control of a single party, known as the *bot herder* or *bot operator*. From one central point, the operator can command every computer on its botnet to simultaneously carry out a coordinated action, which is why botnets are also referred to as *command-and-control (C2)* *systems*.

The scale of a botnet can be many millions of bots. A botnet helps the operator to perform large-scale actions. Because botnets remain under the control of a remote operator, infected machines can receive updates and change their behavior on the fly. As a result, for significant financial gain, C2 systems can rent access to segments of their botnet on the black market.

The prevalence of botnets has continued to grow. It is considered by experts to be the favorite tool of bad actors. [Mirai](https://en.wikipedia.org/wiki/Mirai_(malware)) is one of the biggest botnets. It emerged in 2016, is still operational, and is estimated to have infected up to 350,000 Internet of Things (IoT) devices. This botnet has been adapted and used for many types of activities, including distributed denial of service (DDoS) attacks. More recently, bad actors tried to further obfuscate their activity and source their traffic by obtaining IP addresses through the use of residential proxy services. This creates a legitimate interconnected, peer-to-peer system that adds sophistication to the activity and makes it more challenging to detect and mitigate.

This document focuses on the bot landscape, its effect on your applications, and the available strategies and mitigation options. This prescriptive guidance and its best practices help you understand and mitigate different types of bot attacks. In addition, this guide describes the AWS services and features that support a bot mitigation strategy and how each one can help you protect your applications. It also includes an overview of bot monitoring and best practices for optimizing solution costs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
