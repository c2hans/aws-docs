---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_SwapEnvironmentCNAMEs.html
---

# SwapEnvironmentCNAMEs
<a name="API_SwapEnvironmentCNAMEs"></a>

Swaps the CNAMEs of two environments.

## Request Parameters
<a name="API_SwapEnvironmentCNAMEs_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DestinationEnvironmentId **
The ID of the destination environment.
 Condition: You must specify at least the `DestinationEnvironmentID` or the `DestinationEnvironmentName`. You may also specify both. You must specify the `SourceEnvironmentId` with the `DestinationEnvironmentId`.
Type: String
Required: No

 ** DestinationEnvironmentName **
The name of the destination environment.
 Condition: You must specify at least the `DestinationEnvironmentID` or the `DestinationEnvironmentName`. You may also specify both. You must specify the `SourceEnvironmentName` with the `DestinationEnvironmentName`.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 40.
Required: No

 ** SourceEnvironmentId **
The ID of the source environment.
 Condition: You must specify at least the `SourceEnvironmentID` or the `SourceEnvironmentName`. You may also specify both. If you specify the `SourceEnvironmentId`, you must specify the `DestinationEnvironmentId`.
Type: String
Required: No

 ** SourceEnvironmentName **
The name of the source environment.
 Condition: You must specify at least the `SourceEnvironmentID` or the `SourceEnvironmentName`. You may also specify both. If you specify the `SourceEnvironmentName`, you must specify the `DestinationEnvironmentName`.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 40.
Required: No

## Errors
<a name="API_SwapEnvironmentCNAMEs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_SwapEnvironmentCNAMEs_Examples"></a>

### Example
<a name="API_SwapEnvironmentCNAMEs_Example_1"></a>

This example illustrates one usage of SwapEnvironmentCNAMEs.

#### Sample Request
<a name="API_SwapEnvironmentCNAMEs_Example_1_Request"></a>

```
https://elasticbeanstalk.us-west-2.amazonaws.com/?SourceEnvironmentName=SampleApp
&DestinationEnvironmentName=SampleApp2
&Operation=SwapEnvironmentCNAMEs
&AuthParams
```

#### Sample Response
<a name="API_SwapEnvironmentCNAMEs_Example_1_Response"></a>

```
<SwapEnvironmentCNAMEsResponse xmlns="http://elasticbeanstalk.amazonaws.com/docs/2010-12-01/">
  <ResponseMetadata>
    <RequestId>f4e1b145-9080-11e0-8e5a-a558e0ce1fc4</RequestId>
  </ResponseMetadata>
</SwapEnvironmentCNAMEsResponse>
```

## See Also
<a name="API_SwapEnvironmentCNAMEs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/SwapEnvironmentCNAMEs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/SwapEnvironmentCNAMEs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/SwapEnvironmentCNAMEs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/SwapEnvironmentCNAMEs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/SwapEnvironmentCNAMEs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/SwapEnvironmentCNAMEs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/SwapEnvironmentCNAMEs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/SwapEnvironmentCNAMEs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/SwapEnvironmentCNAMEs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/SwapEnvironmentCNAMEs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
