---
source_url: https://docs.aws.amazon.com/rfdk/latest/guide/work-with-rfdk-typescript.html
---

# Working with the RFDK in TypeScript
<a name="work-with-rfdk-typescript"></a>

**Important**
On November 7, 2025, AWS Thinkbox Deadline 10 will enter maintenance mode. We recommend exploring [AWS Deadline Cloud](https://aws.amazon.com/deadline-cloud/) for render management. For questions, contact [support@awsthinkbox.zendesk.com](mailto:support@awsthinkbox.zendesk.com) or refer to the [Maintenance Mode FAQ](https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/maintenance-mode-faq.html).

## Installing peer dependencies
<a name="typescript-installpeerdeps"></a>

The following command (requires [jq](https://stedolan.github.io/jq/)) installs all of the peer dependencies required by RFDK. Run it from the root of your CDK application directory.

```
npm view --json aws-rfdk peerDependencies | jq '. | to_entries[] | .key + "@" + .value' | xargs npm i --save
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Render Farm Deployment Kit on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rfdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
