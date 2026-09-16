---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateDelegationRequest.html
---

# CreateDelegationRequest
<a name="API_CreateDelegationRequest"></a>

Creates an IAM delegation request for temporary access delegation.

This API is not available for general use. In order to use this API, a caller first need to go through an onboarding process described in the [partner onboarding documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-temporary-delegation-partner-guide.html).

## Request Parameters
<a name="API_CreateDelegationRequest_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Description **
A description of the delegation request.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u00A1-\u00FF]*`
Required: Yes

 ** NotificationChannel **
The notification channel for updates about the delegation request.
At this time,only SNS topic ARNs are accepted for notification. This topic ARN must have a resource policy granting `SNS:Publish` permission to the IAM service principal (`iam.amazonaws.com`). See [partner onboarding documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-temporary-delegation-partner-guide.html) for more details.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 400.
Pattern: `^[a-zA-Z0-9:_.-]+$`
Required: Yes

 ** OnlySendByOwner **
Specifies whether the delegation token should only be sent by the owner.
This flag prevents any party other than the owner from calling `SendDelegationToken` API for this delegation request. This behavior becomes useful when the delegation request owner needs to be present for subsequent partner interactions, but the delegation request was sent to a more privileged user for approval due to the owner lacking sufficient delegation permissions.
Type: Boolean
Required: No

 ** OwnerAccountId **
The AWS account ID this delegation request is targeted to.
If the account ID is not known, this parameter can be omitted, resulting in a request that can be associated by any account. If the account ID passed, then the created delegation request can only be associated with an identity of that target account.
Type: String
Pattern: `\d{12}`
Required: No

 ** Permissions **
The permissions to be delegated in this delegation request.
Type: [DelegationPermission](API_DelegationPermission.md) object
Required: Yes

 ** RedirectUrl **
The URL to redirect to after the delegation request is processed.
This URL is used by the IAM console to show a link to the customer to re-load the partner workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^http(s?)://[a-zA-Z0-9._/-]*(\?[a-zA-Z0-9._=&-]*)?(#[a-zA-Z0-9._/-]*)?$`
Required: No

 ** RequestMessage **
A message explaining the reason for the delegation request.
Requesters can utilize this field to add a custom note to the delegation request. This field is different from the description such that this is to be utilized for a custom messaging on a case-by-case basis.
For example, if the current delegation request is in response to a previous request being rejected, this explanation can be added to the request via this field.
Type: String
Length Constraints: Maximum length of 200.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u00A1-\u00FF]*`
Required: No

 ** RequestorWorkflowId **
The workflow ID associated with the requestor.
This is the unique identifier on the partner side that can be used to track the progress of the request.
IAM maintains a uniqueness check on this workflow id for each request - if a workflow id for an existing request is passed, this API call will fail.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 400.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u00A1-\u00FF]+`
Required: Yes

 ** SessionDuration **
The duration for which the delegated session should remain active, in seconds.
The active time window for the session starts when the customer calls the [SendDelegationToken](https://docs.aws.amazon.com/IAM/latest/APIReference/API_SendDelegationToken.html) API.
Type: Integer
Valid Range: Minimum value of 300. Maximum value of 43200.
Required: Yes

## Response Elements
<a name="API_CreateDelegationRequest_ResponseElements"></a>

The following elements are returned by the service.

 ** ConsoleDeepLink **
A deep link URL to the AWS Management Console for managing the delegation request.
For a console based workflow, partners should redirect the customer to this URL. If the customer is not logged in to any AWS account, the AWS workflow will automatically direct the customer to log in and then display the delegation request approval page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** DelegationRequestId **
The unique identifier for the created delegation request.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 128.
Pattern: `[\w-]+`

## Errors
<a name="API_CreateDelegationRequest_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModification **
The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
HTTP Status Code: 409

 ** EntityAlreadyExists **
The request was rejected because it attempted to create a resource that already exists.
HTTP Status Code: 409

 ** InvalidInput **
The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
HTTP Status Code: 400

 ** LimitExceeded **
The request was rejected because it attempted to create resources beyond the current AWS account limits. The error message describes the limit exceeded.
HTTP Status Code: 409

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_CreateDelegationRequest_Examples"></a>

### Example
<a name="API_CreateDelegationRequest_Example_1"></a>

This example illustrates one usage of CreateDelegationRequest.

#### Sample Request
<a name="API_CreateDelegationRequest_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=CreateDelegationRequest
&Description=Example%20Request
&NotificationChannel=arn%3Aaws%3Asns%3Aus-east-2%3A112233445566%3ADelegationNotificationTopic
&Permissions.PolicyTemplateArn=arn%3Aaws%3Aiam%3A%3A%3Adelegation-template%2Fpartner_delegation_template
&RequestorWorkflowId=requestor-unique-id-1
&SessionDuration=3600
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateDelegationRequest_Example_1_Response"></a>

```
<CreateDelegationRequestResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <CreateDelegationRequestResult>
    <DelegationRequestId>e4bdcdae-4f66-11eD-ELEG-ATIONEXAMPLE</DelegationRequestId>
    <ConsoleDeepLink>https://us-east-1.console.aws.amazon.com/iam/account-access-requests/review/e4bdcdae-4f66-11e4-dele-gationEXAMPLE</ConsoleDeepLink>
  </CreateDelegationRequestResult>
  <ResponseMetadata>
    <RequestId>e4bdcdae-4f66-11e4-aefa-bfd6aEXAMPLE</RequestId>
  </ResponseMetadata>
</CreateDelegationRequestResponse>
```

## See Also
<a name="API_CreateDelegationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/CreateDelegationRequest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/CreateDelegationRequest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/CreateDelegationRequest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/CreateDelegationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/CreateDelegationRequest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/CreateDelegationRequest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/CreateDelegationRequest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/CreateDelegationRequest)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/CreateDelegationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/CreateDelegationRequest)
