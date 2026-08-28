---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsAppSyncGraphQlApiUserPoolConfigDetails.html
---

# AwsAppSyncGraphQlApiUserPoolConfigDetails
<a name="API_AwsAppSyncGraphQlApiUserPoolConfigDetails"></a>

 Specifies the authorization configuration for using Amazon Cognito user pools with your AWS AppSync GraphQL API endpoint.

## Contents
<a name="API_AwsAppSyncGraphQlApiUserPoolConfigDetails_Contents"></a>

 ** AppIdClientRegex **   <a name="securityhub-Type-AwsAppSyncGraphQlApiUserPoolConfigDetails-AppIdClientRegex"></a>
 A regular expression for validating the incoming Amazon Cognito user pools app client ID. If this value isn't set, no filtering is applied.
Type: String
Pattern: `.*\S.*`
Required: No

 ** AwsRegion **   <a name="securityhub-Type-AwsAppSyncGraphQlApiUserPoolConfigDetails-AwsRegion"></a>
 The AWS Region in which the user pool was created.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DefaultAction **   <a name="securityhub-Type-AwsAppSyncGraphQlApiUserPoolConfigDetails-DefaultAction"></a>
 The action that you want your GraphQL API to take when a request that uses Amazon Cognito user pools authentication doesn't match the Amazon Cognito user pools configuration.
Type: String
Pattern: `.*\S.*`
Required: No

 ** UserPoolId **   <a name="securityhub-Type-AwsAppSyncGraphQlApiUserPoolConfigDetails-UserPoolId"></a>
 The user pool ID.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsAppSyncGraphQlApiUserPoolConfigDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsAppSyncGraphQlApiUserPoolConfigDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsAppSyncGraphQlApiUserPoolConfigDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsAppSyncGraphQlApiUserPoolConfigDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
