---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateShareInvitation.html
---

# UpdateShareInvitation
<a name="API_UpdateShareInvitation"></a>

Update a workload or custom lens share invitation.

**Note**
This API operation can be called independently of any resource. Previous documentation implied that a workload ARN must be specified.

## Request Syntax
<a name="API_UpdateShareInvitation_RequestSyntax"></a>

```
PATCH /shareInvitations/{{ShareInvitationId}} HTTP/1.1
Content-type: application/json

{
   "ShareInvitationAction": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateShareInvitation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ShareInvitationId](#API_UpdateShareInvitation_RequestSyntax) **   <a name="wellarchitected-UpdateShareInvitation-request-uri-ShareInvitationId"></a>
The ID assigned to the share invitation.
Pattern: `[0-9a-f]{32}`
Required: Yes

## Request Body
<a name="API_UpdateShareInvitation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ShareInvitationAction](#API_UpdateShareInvitation_RequestSyntax) **   <a name="wellarchitected-UpdateShareInvitation-request-ShareInvitationAction"></a>
Share invitation action taken by contributor.
Type: String
Valid Values: `ACCEPT | REJECT`
Required: Yes

## Response Syntax
<a name="API_UpdateShareInvitation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ShareInvitation": {
      "LensAlias": "string",
      "LensArn": "string",
      "ProfileArn": "string",
      "ShareInvitationId": "string",
      "ShareResourceType": "string",
      "TemplateArn": "string",
      "WorkloadId": "string"
   }
}
```

## Response Elements
<a name="API_UpdateShareInvitation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ShareInvitation](#API_UpdateShareInvitation_ResponseSyntax) **   <a name="wellarchitected-UpdateShareInvitation-response-ShareInvitation"></a>
The updated workload or custom lens share invitation.
Type: [ShareInvitation](API_ShareInvitation.md) object

## Errors
<a name="API_UpdateShareInvitation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** Message **
Description of the error.
HTTP Status Code: 403

 ** ConflictException **
The resource has already been processed, was deleted, or is too large.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 409

 ** InternalServerException **
There is a problem with the AWS Well-Architected Tool API service.
 ** Message **
Description of the error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource was not found.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **
Request was denied due to request throttling.
 ** Message **
Description of the error.
 ** QuotaCode **
Service Quotas requirement to identify originating quota.
 ** ServiceCode **
Service Quotas requirement to identify originating service.
HTTP Status Code: 429

 ** ValidationException **
The user input is not valid.
 ** Fields **
The fields that caused the error, if applicable.
 ** Message **
Description of the error.
 ** Reason **
The reason why the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_UpdateShareInvitation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/UpdateShareInvitation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/UpdateShareInvitation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/UpdateShareInvitation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/UpdateShareInvitation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/UpdateShareInvitation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/UpdateShareInvitation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/UpdateShareInvitation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/UpdateShareInvitation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/UpdateShareInvitation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/UpdateShareInvitation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected Tool. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
