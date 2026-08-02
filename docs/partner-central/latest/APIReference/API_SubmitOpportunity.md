---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_SubmitOpportunity.html
---

# SubmitOpportunity
<a name="API_SubmitOpportunity"></a>

Use this action to submit an Opportunity that was previously created by partner for AWS review. After you perform this action, the Opportunity becomes non-editable until it is reviewed by AWS and has ` LifeCycle.ReviewStatus ` as either `Approved` or `Action Required`.

## Request Syntax
<a name="API_SubmitOpportunity_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "Identifier": "{{string}}",
   "InvolvementType": "{{string}}",
   "Visibility": "{{string}}"
}
```

## Request Parameters
<a name="API_SubmitOpportunity_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_SubmitOpportunity_RequestSyntax) **   <a name="AWSPartnerCentral-SubmitOpportunity-request-Catalog"></a>
Specifies the catalog related to the request. Valid values are:
+ AWS: Submits the opportunity request from the production AWS environment.
+ Sandbox: Submits the opportunity request from a sandbox environment used for testing or development purposes.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [Identifier](#API_SubmitOpportunity_RequestSyntax) **   <a name="AWSPartnerCentral-SubmitOpportunity-request-Identifier"></a>
The identifier of the Opportunity previously created by partner and needs to be submitted.
Type: String
Pattern: `O[0-9]{1,19}`
Required: Yes

 ** [InvolvementType](#API_SubmitOpportunity_RequestSyntax) **   <a name="AWSPartnerCentral-SubmitOpportunity-request-InvolvementType"></a>
Specifies the level of AWS sellers' involvement on the opportunity. Valid values:
+  `Co-sell`: Indicates the user wants to co-sell with AWS. Share the opportunity with AWS to receive deal assistance and support.
+  `For Visibility Only`: Indicates that the user does not need support from AWS Sales Rep. Share this opportunity with AWS for visibility only, you will not receive deal assistance and support.
Type: String
Valid Values: `For Visibility Only | Co-Sell`
Required: Yes

 ** [Visibility](#API_SubmitOpportunity_RequestSyntax) **   <a name="AWSPartnerCentral-SubmitOpportunity-request-Visibility"></a>
Determines whether to restrict visibility of the opportunity from AWS sales. Default value is Full. Valid values:
+  `Full`: The opportunity is fully visible to AWS sales.
+  `Limited`: The opportunity has restricted visibility to AWS sales.
Type: String
Valid Values: `Full | Limited`
Required: No

## Response Elements
<a name="API_SubmitOpportunity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_SubmitOpportunity_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
This error occurs when you don't have permission to perform the requested action.
You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.
 ** Reason **
The reason why access was denied for the requested operation.
HTTP Status Code: 400

 ** InternalServerException **
This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.
Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.
HTTP Status Code: 500

 ** ResourceNotFoundException **
This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.
Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.
HTTP Status Code: 400

 ** ThrottlingException **
This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.
This error occurs when there are too many requests sent. Review the provided [Quotas](https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html) and retry after the provided delay.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by the service or business validation rules.
Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.
 ** ErrorList **
A list of issues that were discovered in the submitted request or the resource state.
 ** Reason **
The primary reason for this validation exception to occur.
+  *REQUEST\_VALIDATION\_FAILED:* The request format is not valid.

  Fix: Verify your request payload includes all required fields, uses correct data types and string formats.
+  *BUSINESS\_VALIDATION\_FAILED:* The requested change doesn't pass the business validation rules.

  Fix: Check that your change aligns with the business rules defined by AWS Partner Central.
HTTP Status Code: 400

## See Also
<a name="API_SubmitOpportunity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/SubmitOpportunity)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/SubmitOpportunity)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/SubmitOpportunity)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/SubmitOpportunity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/SubmitOpportunity)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/SubmitOpportunity)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/SubmitOpportunity)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/SubmitOpportunity)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/SubmitOpportunity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/SubmitOpportunity)
