---
source_url: https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_ListResourceRequests.html
---

# ListResourceRequests
<a name="API_ListResourceRequests"></a>

Returns existing resource operation requests. This includes requests of all status types. For more information, see [Listing active resource operation requests](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-manage-requests.html#resource-operations-manage-requests-list) in the * AWS Cloud Control API User Guide*.

**Note**
Resource operation requests expire after 7 days.

## Request Syntax
<a name="API_ListResourceRequests_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ResourceRequestStatusFilter": {
      "Operations": [ "{{string}}" ],
      "OperationStatuses": [ "{{string}}" ]
   }
}
```

## Request Parameters
<a name="API_ListResourceRequests_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListResourceRequests_RequestSyntax) **   <a name="ccapi-ListResourceRequests-request-MaxResults"></a>
The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a `NextToken` value that you can assign to the `NextToken` request parameter to get the next set of results.
The default is `20`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListResourceRequests_RequestSyntax) **   <a name="ccapi-ListResourceRequests-request-NextToken"></a>
If the previous paginated request didn't return all of the remaining results, the response object's `NextToken` parameter value is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object's `NextToken` parameter. If there are no remaining results, the previous response object's `NextToken` parameter is set to `null`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[-A-Za-z0-9+/=]+`
Required: No

 ** [ResourceRequestStatusFilter](#API_ListResourceRequests_RequestSyntax) **   <a name="ccapi-ListResourceRequests-request-ResourceRequestStatusFilter"></a>
The filter criteria to apply to the requests returned.
Type: [ResourceRequestStatusFilter](API_ResourceRequestStatusFilter.md) object
Required: No

## Response Syntax
<a name="API_ListResourceRequests_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ResourceRequestStatusSummaries": [
      {
         "ErrorCode": "string",
         "EventTime": number,
         "HooksRequestToken": "string",
         "Identifier": "string",
         "Operation": "string",
         "OperationStatus": "string",
         "RequestToken": "string",
         "ResourceModel": "string",
         "RetryAfter": number,
         "StatusMessage": "string",
         "TypeName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListResourceRequests_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListResourceRequests_ResponseSyntax) **   <a name="ccapi-ListResourceRequests-response-NextToken"></a>
If the request doesn't return all of the remaining results, `NextToken` is set to a token. To retrieve the next set of results, call `ListResources` again and assign that token to the request object's `NextToken` parameter. If the request returns all results, `NextToken` is set to null.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[-A-Za-z0-9+/=]+`

 ** [ResourceRequestStatusSummaries](#API_ListResourceRequests_ResponseSyntax) **   <a name="ccapi-ListResourceRequests-response-ResourceRequestStatusSummaries"></a>
The requests that match the specified filter criteria.
Type: Array of [ProgressEvent](API_ProgressEvent.md) objects

## Errors
<a name="API_ListResourceRequests_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ListResourceRequests_Examples"></a>

### ListResourceRequests
<a name="API_ListResourceRequests_Example_1"></a>

The following example returns all current resource requests. In this case, this includes a successful `create` and `update` of a resource, in addition to a `create` operation that failed because a resource of the specified name already exists.

#### Sample Request
<a name="API_ListResourceRequests_Example_1_Request"></a>

```
https://cloudcontrolapi.us-east-1.amazonaws.com/
 ?Action=ListResourceRequests
 &Version=2021-09-30
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20250316T233349Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response
<a name="API_ListResourceRequests_Example_1_Response"></a>

```
<ListResourceRequestsResponse xmlns="http://cloudcontrol.amazonaws.com/doc/2021-09-30/">
  <ListResourceRequestsResult>
    <RequestStatusSummaries>
      <member>
        <Identifier>LogGroupResourceExample2</Identifier>
        <OperationStatus>SUCCESS</OperationStatus>
        <TypeName>AWS::Logs::LogGroup</TypeName>
        <EventTime>2025-02-27T19:23:56.094Z</EventTime>
        <RequestToken>6233b409-a77d-4125-85ee-fd0123456789</RequestToken>
        <Operation>UPDATE</Operation>
      </member>
      <member>
        <Identifier>LogGroupResourceExample2</Identifier>
        <OperationStatus>SUCCESS</OperationStatus>
        <TypeName>AWS::Logs::LogGroup</TypeName>
        <EventTime>2025-02-27T18:01:42.788Z</EventTime>
        <RequestToken>71d8afe7-7e83-4136-92f6-420123456789</RequestToken>
        <Operation>CREATE</Operation>
      </member>
      <member>
        <Identifier>LogGroupResourceExample</Identifier>
        <OperationStatus>SUCCESS</OperationStatus>
        <TypeName>AWS::Logs::LogGroup</TypeName>
        <EventTime>2025-02-27T18:52:57.406Z</EventTime>
        <RequestToken>b4a1cc5a-a2ae-4dec-9e1e-150123456789</RequestToken>
        <Operation>CREATE</Operation>
      </member>
      <member>
        <Identifier>LogGroupResourceExample2</Identifier>
        <OperationStatus>FAILED</OperationStatus>
        <TypeName>AWS::Logs::LogGroup</TypeName>
        <EventTime>2025-02-27T18:07:17.005Z</EventTime>
        <ErrorCode>AlreadyExists</ErrorCode>
        <RequestToken>f2fcf5a1-7f17-4c7a-b67f-ab0123456789</RequestToken>
        <Operation>CREATE</Operation>
        <StatusMessage>Resource of type 'AWS::Logs::LogGroup' with identifier '{"/properties/LogGroupName":"LogGroupResourceExample2"}' already exists.</StatusMessage>
      </member>
    </RequestStatusSummaries>
  </ListResourceRequestsResult>
```

### Filtering ListResourceRequests
<a name="API_ListResourceRequests_Example_2"></a>

The following example returns only the current resource requests for `create` and `update` operations that have failed.

#### Sample Request
<a name="API_ListResourceRequests_Example_2_Request"></a>

```
https://cloudcontrolapi.us-east-1.amazonaws.com/
 ?Action=ListResourceRequests
 &RequestStatusFilter.OperationStatuses.member.1=FAILED
 &RequestStatusFilter.Operations.member.1=CREATE
 &RequestStatusFilter.Operations.member.2=UPDATE
 &Version=2021-09-30
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20250316T233349Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response
<a name="API_ListResourceRequests_Example_2_Response"></a>

```
<ListResourceRequestsResponse xmlns="http://cloudcontrol.amazonaws.com/doc/2021-09-30/">
  <ListResourceRequestsResult>
    <RequestStatusSummaries>
      <member>
        <Identifier>LogGroupResourceExample</Identifier>
        <OperationStatus>FAILED</OperationStatus>
        <EventTime>2025-02-27T18:07:17.005Z</EventTime>
        <TypeName>AWS::Logs::LogGroup</TypeName>
        <ErrorCode>AlreadyExists</ErrorCode>
        <RequestToken>f2fcf5a1-7f17-4c7a-b67f-ab0123456789</RequestToken>
        <Operation>CREATE</Operation>
        <StatusMessage>Resource of type 'AWS::Logs::LogGroup' with identifier '{"/properties/LogGroupName":"LogGroupResourceExample"}' already exists.</StatusMessage>
      </member>
    </RequestStatusSummaries>
  </ListResourceRequestsResult>
  <ResponseMetadata>
    <RequestId>34748e01-2885-4410-90a6-870123456789</RequestId>
  </ResponseMetadata>
</ListResourceRequestsResponse>
```

## See Also
<a name="API_ListResourceRequests_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudcontrol-2021-09-30/ListResourceRequests)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudcontrol-2021-09-30/ListResourceRequests)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudcontrol-2021-09-30/ListResourceRequests)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudcontrol-2021-09-30/ListResourceRequests)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudcontrol-2021-09-30/ListResourceRequests)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudcontrol-2021-09-30/ListResourceRequests)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudcontrol-2021-09-30/ListResourceRequests)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudcontrol-2021-09-30/ListResourceRequests)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudcontrol-2021-09-30/ListResourceRequests)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudcontrol-2021-09-30/ListResourceRequests)
