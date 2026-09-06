---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/startup-resiliency-baseline/stage-3.html
---

# Stage 3: Evaluate and test
<a name="stage-3"></a>

You've built a resilient foundation, but how do you know it actually works? Testing resilience might sound like a luxury when you're racing to prove product-market fit. However, there's a smart way to do this without derailing your feature development. This chapter describes lean, practical testing that fits a startup's pace.

Start with [AWS Resilience Hub](https://docs.aws.amazon.com/resilience-hub/latest/userguide/what-is.html), and think of it as an initial architecture assessment tool. It provides a helpful baseline review of an architecture's resilience foundations. It helps you evaluate if the basic infrastructure setup aligns with your recovery objectives by checking common configuration patterns and potential single points of failure. It can flag obvious gaps, such as missing multiple Availability Zone configurations or incomplete backup policies. Resilience Hub complements, but doesn't replace, thoughtful architecture reviews and targeted testing of critical paths.

To validate your documented recovery objectives, schedule monthly restore tests in [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) in your development environment. Even though it requires engineering time, it might be cheaper than discovering your backups don't work during a real incident. Make it part of your regular development cycle, like running unit tests or code reviews. The goal isn't perfection; it's confidence that you can recover when you need to.

As your startup grows and customers start depending on you more heavily, gradually level up your testing game. When you're deploying new features, include basic resilience checks in your pipeline. Try simple chaos experiments by using [AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html). Start in your preproduction environment and start small. Test how your application handles a delayed API response in development before considering any production experiments. As your confidence grows, gradually expand these tests, but always validate in preproduction first. For a startup, breaking things in production is risky enough without doing it intentionally.

The key is balance. Every hour spent on testing is an hour not spent building new features. But a few strategic tests can prevent the kinds of outages that lose customer trust. Use automated tools provided by AWS to do the heavy lifting, and focus on the testing that matters most to your customers. This helps you build confidence in your application's resilience without slowing innovation.

The next chapter explores how to evolve this foundation as your startup scales.
