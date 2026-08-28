---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEntityAggregates.html
---

# DescribeEntityAggregates
<a name="API_DescribeEntityAggregates"></a>

Returns the number of entities that are affected by each of the specified events.

## Request Syntax
<a name="API_DescribeEntityAggregates_RequestSyntax"></a>

```
{
   "eventArns": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeEntityAggregates_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [eventArns](#API_DescribeEntityAggregates_RequestSyntax) **   <a name="AWSHealth-DescribeEntityAggregates-request-eventArns"></a>
A list of event ARNs (unique identifiers). For example: `"arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456", "arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"`
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+(-[a-z]+)?)?:health:[^:]*:[^:]*:event(?:/[\w-]+){3}`
Required: No

## Response Syntax
<a name="API_DescribeEntityAggregates_ResponseSyntax"></a>

```
{
   "entityAggregates": [
      {
         "count": number,
         "eventArn": "string",
         "statuses": {
            "string" : number
         }
      }
   ]
}
```

## Response Elements
<a name="API_DescribeEntityAggregates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [entityAggregates](#API_DescribeEntityAggregates_ResponseSyntax) **   <a name="AWSHealth-DescribeEntityAggregates-response-entityAggregates"></a>
The number of entities that are affected by each of the specified events.
Type: Array of [EntityAggregate](API_EntityAggregate.md) objects

## Errors
<a name="API_DescribeEntityAggregates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeEntityAggregates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/health-2016-08-04/DescribeEntityAggregates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/health-2016-08-04/DescribeEntityAggregates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/DescribeEntityAggregates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/health-2016-08-04/DescribeEntityAggregates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/DescribeEntityAggregates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/health-2016-08-04/DescribeEntityAggregates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/health-2016-08-04/DescribeEntityAggregates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/health-2016-08-04/DescribeEntityAggregates)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/health-2016-08-04/DescribeEntityAggregates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/DescribeEntityAggregates)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query health` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
