---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/how-aws-solution-for-prebid-server-works.html
---

# How Guidance for Deploying a Prebid Server on AWS works
<a name="how-aws-solution-for-prebid-server-works"></a>

## Workflow of banner ads
<a name="workflow-of-banner-ads"></a>

From [docs.prebid.org](https://docs.prebid.org/prebid-server/use-cases/pbs-pbjs.html).

 **Workflow diagram of banner ads**

![workflow](http://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/images/workflow.png)

1.  `Prebid.js` is set up to run auctions for one or more bidders through `s2sConfig`.

1. Prebid Server parses the request and holds the auction.

1. The response, including the body of the winning creative(s), is sent back to the browser.

1.  `Prebid.js` passes ad server targeting variables to the page, which forwards it to the ad server.

1. When a header bidding ad wins, the ad server responds to the page with the [Prebid Universal Creative](https://github.com/prebid/prebid-universal-creative), which calls the render function in Prebid.js.

1. The render function displays the creative.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Deploying a Prebid Server on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
