---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ResetConnectorMetadataCache.html
---

# ResetConnectorMetadataCache
<a name="API_ResetConnectorMetadataCache"></a>

Resets metadata about your connector entities that Amazon AppFlow stored in its cache. Use this action when you want Amazon AppFlow to return the latest information about the data that you have in a source application.

Amazon AppFlow returns metadata about your entities when you use the ListConnectorEntities or DescribeConnectorEntities actions. Following these actions, Amazon AppFlow caches the metadata to reduce the number of API requests that it must send to the source application. Amazon AppFlow automatically resets the cache once every hour, but you can use this action when you want to get the latest metadata right away.

## Request Syntax
<a name="API_ResetConnectorMetadataCache_RequestSyntax"></a>

```
POST /reset-connector-metadata-cache HTTP/1.1
Content-type: application/json

{
   "apiVersion": "{{string}}",
   "connectorEntityName": "{{string}}",
   "connectorProfileName": "{{string}}",
   "connectorType": "{{string}}",
   "entitiesPath": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ResetConnectorMetadataCache_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ResetConnectorMetadataCache_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [apiVersion](#API_ResetConnectorMetadataCache_RequestSyntax) **   <a name="appflow-ResetConnectorMetadataCache-request-apiVersion"></a>
The API version that you specified in the connector profile that you’re resetting cached metadata for. You must use this parameter only if the connector supports multiple API versions or if the connector type is CustomConnector.
To look up how many versions a connector supports, use the DescribeConnectors action. In the response, find the value that Amazon AppFlow returns for the connectorVersion parameter.
To look up the connector type, use the DescribeConnectorProfiles action. In the response, find the value that Amazon AppFlow returns for the connectorType parameter.
To look up the API version that you specified in a connector profile, use the DescribeConnectorProfiles action.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `\S+`
Required: No

 ** [connectorEntityName](#API_ResetConnectorMetadataCache_RequestSyntax) **   <a name="appflow-ResetConnectorMetadataCache-request-connectorEntityName"></a>
Use this parameter if you want to reset cached metadata about the details for an individual entity.
If you don't include this parameter in your request, Amazon AppFlow only resets cached metadata about entity names, not entity details.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `\S+`
Required: No

 ** [connectorProfileName](#API_ResetConnectorMetadataCache_RequestSyntax) **   <a name="appflow-ResetConnectorMetadataCache-request-connectorProfileName"></a>
The name of the connector profile that you want to reset cached metadata for.
You can omit this parameter if you're resetting the cache for any of the following connectors: Connect Customer, Amazon EventBridge, Amazon Lookout for Metrics, Amazon S3, or Upsolver. If you're resetting the cache for any other connector, you must include this parameter in your request.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[\w/!@#+=.-]+`
Required: No

 ** [connectorType](#API_ResetConnectorMetadataCache_RequestSyntax) **   <a name="appflow-ResetConnectorMetadataCache-request-connectorType"></a>
The type of connector to reset cached metadata for.
You must include this parameter in your request if you're resetting the cache for any of the following connectors: Connect Customer, Amazon EventBridge, Amazon Lookout for Metrics, Amazon S3, or Upsolver. If you're resetting the cache for any other connector, you can omit this parameter from your request.
Type: String
Valid Values: `Salesforce | Singular | Slack | Redshift | S3 | Marketo | Googleanalytics | Zendesk | Servicenow | Datadog | Trendmicro | Snowflake | Dynatrace | Infornexus | Amplitude | Veeva | EventBridge | LookoutMetrics | Upsolver | Honeycode | CustomerProfiles | SAPOData | CustomConnector | Pardot`
Required: No

 ** [entitiesPath](#API_ResetConnectorMetadataCache_RequestSyntax) **   <a name="appflow-ResetConnectorMetadataCache-request-entitiesPath"></a>
Use this parameter only if you’re resetting the cached metadata about a nested entity. Only some connectors support nested entities. A nested entity is one that has another entity as a parent. To use this parameter, specify the name of the parent entity.
To look up the parent-child relationship of entities, you can send a ListConnectorEntities request that omits the entitiesPath parameter. Amazon AppFlow will return a list of top-level entities. For each one, it indicates whether the entity has nested entities. Then, in a subsequent ListConnectorEntities request, you can specify a parent entity name for the entitiesPath parameter. Amazon AppFlow will return a list of the child entities for that parent.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[\s\w/!@#+=,.-]*`
Required: No

## Response Syntax
<a name="API_ResetConnectorMetadataCache_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_ResetConnectorMetadataCache_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_ResetConnectorMetadataCache_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
 There was a conflict when processing the request (for example, a flow with the given name already exists within the account. Check for conflicting resource names and try again.
HTTP Status Code: 409

 ** InternalServerException **
 An internal service error occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The resource specified in the request (such as the source or destination connector profile) is not found.
HTTP Status Code: 404

 ** ValidationException **
 The request has invalid or missing parameters.
HTTP Status Code: 400

## Examples
<a name="API_ResetConnectorMetadataCache_Examples"></a>

### Reset cache of entity names
<a name="API_ResetConnectorMetadataCache_Example_1"></a>

The following example shows the request body for a call to reset the cached metadata for entity names.

#### Sample Request
<a name="API_ResetConnectorMetadataCache_Example_1_Request"></a>

```
{
   "apiVersion": "v1.0",
   "connectorProfileName": "MyCustomConnector"
}
```

#### Sample Response
<a name="API_ResetConnectorMetadataCache_Example_1_Response"></a>

```
{}
```

### Reset cache of entity details
<a name="API_ResetConnectorMetadataCache_Example_2"></a>

The following example shows the request body for a call to reset the cached metadata about the details for a specific entity.

#### Sample Request
<a name="API_ResetConnectorMetadataCache_Example_2_Request"></a>

```
{
   "apiVersion": "v1.0",
   "connectorProfileName": "MyCustomConnector",
   "connectorEntityName": "EntityName"
}
```

#### Sample Response
<a name="API_ResetConnectorMetadataCache_Example_2_Response"></a>

```
{}
```

## See Also
<a name="API_ResetConnectorMetadataCache_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appflow-2020-08-23/ResetConnectorMetadataCache)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appflow-2020-08-23/ResetConnectorMetadataCache)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/ResetConnectorMetadataCache)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appflow-2020-08-23/ResetConnectorMetadataCache)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/ResetConnectorMetadataCache)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appflow-2020-08-23/ResetConnectorMetadataCache)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appflow-2020-08-23/ResetConnectorMetadataCache)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appflow-2020-08-23/ResetConnectorMetadataCache)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appflow-2020-08-23/ResetConnectorMetadataCache)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/ResetConnectorMetadataCache)
