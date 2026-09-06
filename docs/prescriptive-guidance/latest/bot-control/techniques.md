---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/bot-control/techniques.html
---

# Techniques for bot control
<a name="techniques"></a>

The main goal of bot mitigation is limiting the negative impact of automated bot activity on an organization's web sites, services, and applications. The technology and techniques used depend on the type of traffic or activity you want to defend against. Understanding the application and its traffic is key to accomplishing this. For more information on where to start, see the [Guidelines for monitoring and visibility](monitoring.md) section in this guide.

In general, the controls that bot mitigation solutions provide can be grouped into the following high-level categories: static, client identification, and advanced analysis. The following figure shows the different techniques available and how they can be used depending on the bot activity complexity. This highlights how the base, or the broadest mitigation, can be obtained through the use of static controls, such as allow listing and intrinsic checks. The smallest portion of bots is always the most advanced, and mitigating against these bots requires more advanced technology and a combination of controls.

![As bot complexity increases, so must the complexity and sophistication of the mitigation techniques.](http://docs.aws.amazon.com/prescriptive-guidance/latest/bot-control/images/guide-img/7c615558-ea52-4b14-ae3f-0e853a88c41f/images/5616f722-6b8f-42f9-b7da-aad3ea6ea551.png)

Next, this guide explores each category and its techniques. It also describes the options that are available in [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) to implement these controls:
+ [Static controls](static-controls.md)
+ [Client identification controls](client-identification-controls.md)
+ [Advanced analysis controls](advanced-analysis-controls.md)
