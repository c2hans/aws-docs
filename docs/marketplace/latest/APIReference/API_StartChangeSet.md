---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_StartChangeSet.html
---

# StartChangeSet
<a name="API_StartChangeSet"></a>

Allows you to request changes for your entities. Within a single `ChangeSet`, you can't start the same change type against the same entity multiple times. Additionally, when a `ChangeSet` is running, all the entities targeted by the different changes are locked until the change set has completed (either succeeded, cancelled, or failed). If you try to start a change set containing a change against an entity that is already locked, you will receive a `ResourceInUseException` error.

For example, you can't start the `ChangeSet` described in the [example](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_StartChangeSet.html#API_StartChangeSet_Examples) later in this topic because it contains two changes to run the same change type (`AddRevisions`) against the same entity (`entity-id@1`).

For more information about working with change sets, see [ Working with change sets](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#working-with-change-sets). For information about change types for single-AMI products, see [Working with single-AMI products](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/ami-products.html#working-with-single-AMI-products). Also, for more information about change types available for container-based products, see [Working with container products](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/container-products.html#working-with-container-products).

To download "DetailsDocument" shapes, see [Python](https://github.com/awslabs/aws-marketplace-catalog-api-shapes-for-python) and [Java](https://github.com/awslabs/aws-marketplace-catalog-api-shapes-for-java/tree/main) shapes on GitHub.

## Request Syntax
<a name="API_StartChangeSet_RequestSyntax"></a>

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
   "Catalog": "{{string}}",
   "ChangeSet": [
      {
         "ChangeName": "{{string}}",
         "ChangeType": "{{string}}",
         "Details": "{{string}}",
         "DetailsDocument": {{JSON value}},
         "Entity": {
            "Identifier": "{{string}}",
            "Type": "{{string}}"
         },
         "EntityTags": [
            {
               "Key": "{{string}}",
               "Value": "{{string}}"
            }
         ]
      }
   ],
   "ChangeSetName": "{{string}}",
   "ChangeSetTags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "ClientRequestToken": "{{string}}",
   "Intent": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartChangeSet_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartChangeSet_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Catalog](#API_StartChangeSet_RequestSyntax) **   <a name="AWSMarketplaceService-StartChangeSet-request-Catalog"></a>
The catalog related to the request. Fixed value: `AWSMarketplace`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z]+$`
Required: Yes

 ** [ChangeSet](#API_StartChangeSet_RequestSyntax) **   <a name="AWSMarketplaceService-StartChangeSet-request-ChangeSet"></a>
Array of `change` object.
Type: Array of [Change](API_Change.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: Yes

 ** [ChangeSetName](#API_StartChangeSet_RequestSyntax) **   <a name="AWSMarketplaceService-StartChangeSet-request-ChangeSetName"></a>
Optional case sensitive string of up to 100 ASCII characters. The change set name can be used to filter the list of change sets.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[\w\s+=.:@-]+$`
Required: No

 ** [ChangeSetTags](#API_StartChangeSet_RequestSyntax) **   <a name="AWSMarketplaceService-StartChangeSet-request-ChangeSetTags"></a>
A list of objects specifying each key name and value for the `ChangeSetTags` property.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

 ** [ClientRequestToken](#API_StartChangeSet_RequestSyntax) **   <a name="AWSMarketplaceService-StartChangeSet-request-ClientRequestToken"></a>
A unique token to identify the request to ensure idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[!-~]+$`
Required: No

 ** [Intent](#API_StartChangeSet_RequestSyntax) **   <a name="AWSMarketplaceService-StartChangeSet-request-Intent"></a>
The intent related to the request. The default is `APPLY`. To test your request before applying changes to your entities, use `VALIDATE`. This feature is currently available for adding versions to single-AMI products. For more information, see [Add a new version](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/ami-products.html#ami-add-version).
Type: String
Valid Values: `VALIDATE | APPLY`
Required: No

## Response Syntax
<a name="API_StartChangeSet_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ChangeSetArn": "string",
   "ChangeSetId": "string"
}
```

## Response Elements
<a name="API_StartChangeSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChangeSetArn](#API_StartChangeSet_ResponseSyntax) **   <a name="AWSMarketplaceService-StartChangeSet-response-ChangeSetArn"></a>
The ARN associated to the unique identifier generated for the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9:*/-]+$`

 ** [ChangeSetId](#API_StartChangeSet_ResponseSyntax) **   <a name="AWSMarketplaceService-StartChangeSet-response-ChangeSetId"></a>
Unique identifier generated for the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[\w\-]+$`

## Errors
<a name="API_StartChangeSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP status code: 403
HTTP Status Code: 403

 ** InternalServiceException **
There was an internal service exception.
HTTP status code: 500
HTTP Status Code: 500

 ** ResourceInUseException **
The resource is currently in use.
HTTP Status Code: 423

 ** ResourceNotFoundException **
The specified resource wasn't found.
HTTP status code: 404
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The maximum number of open requests per account has been exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
Too many requests.
HTTP status code: 429
HTTP Status Code: 429

 ** ValidationException **
An error occurred during validation.
HTTP status code: 422
HTTP Status Code: 422

## Examples
<a name="API_StartChangeSet_Examples"></a>

### Example
<a name="API_StartChangeSet_Example_1"></a>

You can't start this `ChangeSet` because it contains two changes to run the same change type (`AddRevisions`) against the same entity (`entity-id@1)`.

```
{
    "Catalog": "AWSMarketplace",
    "ChangeSetName": "Adding revisions to my test Data Product",
    "ChangeSet": [
        {
            "ChangeType": "AddRevisions",
            "Entity": {
                "Identifier": "entity-id@1",
                "Type": "DataProduct@1.0"
            },
            "Details": "{\"DataSetArn\": \"data-set-arn\", \"RevisionArns\": [\"revision-arn\", \"revision-arn-2\"] }"
        },
        {
            "ChangeType": "AddRevisions",
            "Entity": {
                "Identifier": "entity-id@1",
                "Type": "DataProduct@1.0"
            },
            "Details": "{\"DataSetArn\": \"data-set-arn\", \"RevisionArns\": [\"revision-arn3\"] }"
        }
    ]
}
```

## See Also
<a name="API_StartChangeSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-catalog-2018-09-17/StartChangeSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-catalog-2018-09-17/StartChangeSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/StartChangeSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-catalog-2018-09-17/StartChangeSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/StartChangeSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-catalog-2018-09-17/StartChangeSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-catalog-2018-09-17/StartChangeSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-catalog-2018-09-17/StartChangeSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/marketplace-catalog-2018-09-17/StartChangeSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/StartChangeSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
