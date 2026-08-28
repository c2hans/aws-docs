---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-crawler-recrawlpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Crawler RecrawlPolicy
<a name="aws-properties-glue-crawler-recrawlpolicy"></a>

When crawling an Amazon S3 data source after the first crawl is complete, specifies whether to crawl the entire dataset again or to crawl only folders that were added since the last crawler run. For more information, see [Incremental Crawls in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/incremental-crawls.html) in the developer guide.

## Syntax
<a name="aws-properties-glue-crawler-recrawlpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-crawler-recrawlpolicy-syntax.json"></a>

```
{
  "[RecrawlBehavior](#cfn-glue-crawler-recrawlpolicy-recrawlbehavior)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-crawler-recrawlpolicy-syntax.yaml"></a>

```
  [RecrawlBehavior](#cfn-glue-crawler-recrawlpolicy-recrawlbehavior): {{String}}
```

## Properties
<a name="aws-properties-glue-crawler-recrawlpolicy-properties"></a>

`RecrawlBehavior`  <a name="cfn-glue-crawler-recrawlpolicy-recrawlbehavior"></a>
Specifies whether to crawl the entire dataset again or to crawl only folders that were added since the last crawler run.
A value of `CRAWL_EVERYTHING` specifies crawling the entire dataset again.
A value of `CRAWL_NEW_FOLDERS_ONLY` specifies crawling only folders that were added since the last crawler run.
A value of `CRAWL_EVENT_MODE` specifies crawling only the changes identified by Amazon S3 events.
*Required*: No
*Type*: String
*Allowed values*: `CRAWL_EVERYTHING | CRAWL_NEW_FOLDERS_ONLY | CRAWL_EVENT_MODE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
