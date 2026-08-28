---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/hyperscale-aurora-mysql/introduction.html
---

# Hyperscaling Aurora MySQL-Compatible to handle sudden traffic growth
<a name="introduction"></a>

*Oliver Francis, Vikram singh Rai, and Shyam Sunder Rakhecha, Amazon Web Services*

Your business on the internet might face unprecedented [hypergrowth](https://aws.amazon.com/blogs/architecture/journey-to-adopt-cloud-native-architecture-series-1-preparing-your-applications-for-hypergrowth/), which your existing application infrastructure is not capable of handling. This can happen in response to various factors, such as an advertisement about your product that results in more than expected interest or a sudden shift in customer buying patterns from in-person to online.

To address these unexpected loads, you have to hyperscale your infrastructure. Scaling the application tier entails adding more servers or pods. But the most difficult piece in achieving hyperscaling is the database. You can scale your Database instance to the largest available instance size, but that might not solve your problem.

If you run your database workload on Amazon Aurora MySQL-Compatible Edition, this guide provides recommendations you can implement to hyperscale your database to meet sudden hypergrowth. Not all of these recommendations are long-term best practices. If you expect hypergrowth and have time to plan to address it, see the blog posts that are listed in the *Resources* section. Those posts can help you implement long-term best practices. On the other hand, if you face unexpected hypergrowth, this guide will help you manage your load and achieve reasonable stability while you plan and implement long-term solutions for your business.

Note that the recommendations outlined in this guide will require implementation help from your development team.

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>

The approaches covered in this guide will help you do the following:
+ Stabilize your business in the event of unexpected hypergrowth. Achieve enough stability to implement long-term best practices for hypergrowth.
+ Prevent financial loss. Sudden interruptions on a hyperscaled environment can lead to a drop in business transactions that are performed on your application by your customers. This can lead to substantial financial losses in some cases. A stabilized hyperscaled environment is key to preventing long outages that result in a loss of business.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
