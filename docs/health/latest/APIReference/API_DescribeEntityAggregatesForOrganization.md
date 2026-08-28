---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEntityAggregatesForOrganization.html
---

# DescribeEntityAggregatesForOrganization
<a name="API_DescribeEntityAggregatesForOrganization"></a>

Returns a list of entity aggregates for your AWS Organizations that are affected by each of the specified events.

## Request Syntax
<a name="API_DescribeEntityAggregatesForOrganization_RequestSyntax"></a>

```
{
   "awsAccountIds": [ "{{string}}" ],
   "eventArns": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeEntityAggregatesForOrganization_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [awsAccountIds](#API_DescribeEntityAggregatesForOrganization_RequestSyntax) **   <a name="AWSHealth-DescribeEntityAggregatesForOrganization-request-awsAccountIds"></a>
A list of 12-digit AWS account numbers that contains the affected entities.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Length Constraints: Maximum length of 12.
Pattern: `^\S+$`
Required: No

 ** [eventArns](#API_DescribeEntityAggregatesForOrganization_RequestSyntax) **   <a name="AWSHealth-DescribeEntityAggregatesForOrganization-request-eventArns"></a>
A list of event ARNs (unique identifiers). For example: `"arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456", "arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"`
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Length Constraints: Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+(-[a-z]+)?)?:health:[^:]*:[^:]*:event(?:/[\w-]+){3}`
Required: Yes

## Response Syntax
<a name="API_DescribeEntityAggregatesForOrganization_ResponseSyntax"></a>

```
{
   "organizationEntityAggregates": [
      {
         "accounts": [
            {
               "accountId": "string",
               "count": number,
               "statuses": {
                  "string" : number
               }
            }
         ],
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
<a name="API_DescribeEntityAggregatesForOrganization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [organizationEntityAggregates](#API_DescribeEntityAggregatesForOrganization_ResponseSyntax) **   <a name="AWSHealth-DescribeEntityAggregatesForOrganization-response-organizationEntityAggregates"></a>
The list of entity aggregates for each of the specified accounts that are affected by each of the specified events.
Type: Array of [OrganizationEntityAggregate](API_OrganizationEntityAggregate.md) objects

## Errors
<a name="API_DescribeEntityAggregatesForOrganization_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeEntityAggregatesForOrganization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/health-2016-08-04/DescribeEntityAggregatesForOrganization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/health-2016-08-04/DescribeEntityAggregatesForOrganization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/DescribeEntityAggregatesForOrganization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/health-2016-08-04/DescribeEntityAggregatesForOrganization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/DescribeEntityAggregatesForOrganization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/health-2016-08-04/DescribeEntityAggregatesForOrganization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/health-2016-08-04/DescribeEntityAggregatesForOrganization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/health-2016-08-04/DescribeEntityAggregatesForOrganization)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/health-2016-08-04/DescribeEntityAggregatesForOrganization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/DescribeEntityAggregatesForOrganization)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query health` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
