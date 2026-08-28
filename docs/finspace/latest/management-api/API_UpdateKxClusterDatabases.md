---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_UpdateKxClusterDatabases.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# UpdateKxClusterDatabases
<a name="API_UpdateKxClusterDatabases"></a>

Updates the databases mounted on a kdb cluster, which includes the `changesetId` and all the dbPaths to be cached. This API does not allow you to change a database name or add a database if you created a cluster without one.

Using this API you can point a cluster to a different changeset and modify a list of partitions being cached.

## Request Syntax
<a name="API_UpdateKxClusterDatabases_RequestSyntax"></a>

```
PUT /kx/environments/{{environmentId}}/clusters/{{clusterName}}/configuration/databases HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "databases": [
      {
         "cacheConfigurations": [
            {
               "cacheType": "{{string}}",
               "dataviewName": "{{string}}",
               "dbPaths": [ "{{string}}" ]
            }
         ],
         "changesetId": "{{string}}",
         "databaseName": "{{string}}",
         "dataviewConfiguration": {
            "changesetId": "{{string}}",
            "dataviewName": "{{string}}",
            "dataviewVersionId": "{{string}}",
            "segmentConfigurations": [
               {
                  "dbPaths": [ "{{string}}" ],
                  "onDemand": {{boolean}},
                  "volumeName": "{{string}}"
               }
            ]
         },
         "dataviewName": "{{string}}"
      }
   ],
   "deploymentConfiguration": {
      "deploymentStrategy": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateKxClusterDatabases_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clusterName](#API_UpdateKxClusterDatabases_RequestSyntax) **   <a name="finspace-UpdateKxClusterDatabases-request-uri-clusterName"></a>
A unique name for the cluster that you want to modify.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
Required: Yes

 ** [environmentId](#API_UpdateKxClusterDatabases_RequestSyntax) **   <a name="finspace-UpdateKxClusterDatabases-request-uri-environmentId"></a>
The unique identifier of a kdb environment.
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^[a-z0-9]+$`
Required: Yes

## Request Body
<a name="API_UpdateKxClusterDatabases_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [databases](#API_UpdateKxClusterDatabases_RequestSyntax) **   <a name="finspace-UpdateKxClusterDatabases-request-databases"></a>
 The structure of databases mounted on the cluster.
Type: Array of [KxDatabaseConfiguration](API_KxDatabaseConfiguration.md) objects
Required: Yes

 ** [clientToken](#API_UpdateKxClusterDatabases_RequestSyntax) **   <a name="finspace-UpdateKxClusterDatabases-request-clientToken"></a>
A token that ensures idempotency. This token expires in 10 minutes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-]+$`
Required: No

 ** [deploymentConfiguration](#API_UpdateKxClusterDatabases_RequestSyntax) **   <a name="finspace-UpdateKxClusterDatabases-request-deploymentConfiguration"></a>
 The configuration that allows you to choose how you want to update the databases on a cluster.
Type: [KxDeploymentConfiguration](API_KxDeploymentConfiguration.md) object
Required: No

## Response Syntax
<a name="API_UpdateKxClusterDatabases_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateKxClusterDatabases_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateKxClusterDatabases_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There was a conflict with this action, and it could not be completed.
 ** reason **
The reason for the conflict exception.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** LimitExceededException **
A service limit or quota is exceeded.
HTTP Status Code: 400

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateKxClusterDatabases_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2021-03-12/UpdateKxClusterDatabases)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2021-03-12/UpdateKxClusterDatabases)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/UpdateKxClusterDatabases)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2021-03-12/UpdateKxClusterDatabases)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/UpdateKxClusterDatabases)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2021-03-12/UpdateKxClusterDatabases)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2021-03-12/UpdateKxClusterDatabases)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2021-03-12/UpdateKxClusterDatabases)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/finspace-2021-03-12/UpdateKxClusterDatabases)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/UpdateKxClusterDatabases)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
