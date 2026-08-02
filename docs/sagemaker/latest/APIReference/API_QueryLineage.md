---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_QueryLineage.html
---

# QueryLineage
<a name="API_QueryLineage"></a>

Use this action to inspect your lineage and discover relationships between entities. For more information, see [ Querying Lineage Entities](https://docs.aws.amazon.com/sagemaker/latest/dg/querying-lineage-entities.html) in the *Amazon SageMaker Developer Guide*.

## Request Syntax
<a name="API_QueryLineage_RequestSyntax"></a>

```
{
   "Direction": "{{string}}",
   "Filters": {
      "CreatedAfter": {{number}},
      "CreatedBefore": {{number}},
      "LineageTypes": [ "{{string}}" ],
      "ModifiedAfter": {{number}},
      "ModifiedBefore": {{number}},
      "Properties": {
         "{{string}}" : "{{string}}"
      },
      "Types": [ "{{string}}" ]
   },
   "IncludeEdges": {{boolean}},
   "MaxDepth": {{number}},
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "StartArns": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_QueryLineage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Direction](#API_QueryLineage_RequestSyntax) **   <a name="sagemaker-QueryLineage-request-Direction"></a>
Associations between lineage entities have a direction. This parameter determines the direction from the StartArn(s) that the query traverses.
Type: String
Valid Values: `Both | Ascendants | Descendants`
Required: No

 ** [Filters](#API_QueryLineage_RequestSyntax) **   <a name="sagemaker-QueryLineage-request-Filters"></a>
A set of filtering parameters that allow you to specify which entities should be returned.
+ Properties - Key-value pairs to match on the lineage entities' properties.
+ LineageTypes - A set of lineage entity types to match on. For example: `TrialComponent`, `Artifact`, or `Context`.
+ CreatedBefore - Filter entities created before this date.
+ ModifiedBefore - Filter entities modified before this date.
+ ModifiedAfter - Filter entities modified after this date.
Type: [QueryFilters](API_QueryFilters.md) object
Required: No

 ** [IncludeEdges](#API_QueryLineage_RequestSyntax) **   <a name="sagemaker-QueryLineage-request-IncludeEdges"></a>
 Setting this value to `True` retrieves not only the entities of interest but also the [Associations](https://docs.aws.amazon.com/sagemaker/latest/dg/lineage-tracking-entities.html) and lineage entities on the path. Set to `False` to only return lineage entities that match your query.
Type: Boolean
Required: No

 ** [MaxDepth](#API_QueryLineage_RequestSyntax) **   <a name="sagemaker-QueryLineage-request-MaxDepth"></a>
The maximum depth in lineage relationships from the `StartArns` that are traversed. Depth is a measure of the number of `Associations` from the `StartArn` entity to the matched results.
Type: Integer
Valid Range: Maximum value of 10.
Required: No

 ** [MaxResults](#API_QueryLineage_RequestSyntax) **   <a name="sagemaker-QueryLineage-request-MaxResults"></a>
Limits the number of vertices in the results. Use the `NextToken` in a response to to retrieve the next page of results.
Type: Integer
Valid Range: Maximum value of 50.
Required: No

 ** [NextToken](#API_QueryLineage_RequestSyntax) **   <a name="sagemaker-QueryLineage-request-NextToken"></a>
Limits the number of vertices in the request. Use the `NextToken` in a response to to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: No

 ** [StartArns](#API_QueryLineage_RequestSyntax) **   <a name="sagemaker-QueryLineage-request-StartArns"></a>
A list of resource Amazon Resource Name (ARN) that represent the starting point for your lineage query.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:(experiment|experiment-trial-component|artifact|action|context)/.*`
Required: No

## Response Syntax
<a name="API_QueryLineage_ResponseSyntax"></a>

```
{
   "Edges": [
      {
         "AssociationType": "string",
         "DestinationArn": "string",
         "SourceArn": "string"
      }
   ],
   "NextToken": "string",
   "Vertices": [
      {
         "Arn": "string",
         "LineageType": "string",
         "Type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_QueryLineage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Edges](#API_QueryLineage_ResponseSyntax) **   <a name="sagemaker-QueryLineage-response-Edges"></a>
A list of edges that connect vertices in the response.
Type: Array of [Edge](API_Edge.md) objects

 ** [NextToken](#API_QueryLineage_ResponseSyntax) **   <a name="sagemaker-QueryLineage-response-NextToken"></a>
Limits the number of vertices in the response. Use the `NextToken` in a response to to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.

 ** [Vertices](#API_QueryLineage_ResponseSyntax) **   <a name="sagemaker-QueryLineage-response-Vertices"></a>
A list of vertices connected to the start entity(ies) in the lineage graph.
Type: Array of [Vertex](API_Vertex.md) objects

## Errors
<a name="API_QueryLineage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_QueryLineage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/QueryLineage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/QueryLineage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/QueryLineage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/QueryLineage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/QueryLineage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/QueryLineage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/QueryLineage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/QueryLineage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/QueryLineage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/QueryLineage)
