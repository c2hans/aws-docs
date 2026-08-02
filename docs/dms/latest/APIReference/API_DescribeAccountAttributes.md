---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeAccountAttributes.html
---

# DescribeAccountAttributes
<a name="API_DescribeAccountAttributes"></a>

Lists all of the AWS DMS attributes for a customer account. These attributes include AWS DMS quotas for the account and a unique account identifier in a particular DMS region. DMS quotas include a list of resource quotas supported by the account, such as the number of replication instances allowed. The description for each resource quota, includes the quota name, current usage toward that quota, and the quota's maximum value. DMS uses the unique account identifier to name each artifact used by DMS in the given region.

This command does not take any parameters.

## Response Syntax
<a name="API_DescribeAccountAttributes_ResponseSyntax"></a>

```
{
   "AccountQuotas": [
      {
         "AccountQuotaName": "string",
         "Max": number,
         "Used": number
      }
   ],
   "UniqueAccountIdentifier": "string"
}
```

## Response Elements
<a name="API_DescribeAccountAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccountQuotas](#API_DescribeAccountAttributes_ResponseSyntax) **   <a name="DMS-DescribeAccountAttributes-response-AccountQuotas"></a>
Account quota information.
Type: Array of [AccountQuota](API_AccountQuota.md) objects

 ** [UniqueAccountIdentifier](#API_DescribeAccountAttributes_ResponseSyntax) **   <a name="DMS-DescribeAccountAttributes-response-UniqueAccountIdentifier"></a>
A unique AWS DMS identifier for an account in a particular AWS Region. The value of this identifier has the following format: `c99999999999`. DMS uses this identifier to name artifacts. For example, DMS uses this identifier to name the default Amazon S3 bucket for storing task assessment reports in a given AWS Region. The format of this S3 bucket name is the following: `dms-AccountNumber-UniqueAccountIdentifier.` Here is an example name for this default S3 bucket: `dms-111122223333-c44445555666`.
 AWS DMS supports the `UniqueAccountIdentifier` parameter in versions 3.1.4 and later.
Type: String

## Errors
<a name="API_DescribeAccountAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeAccountAttributes_Examples"></a>

### Example
<a name="API_DescribeAccountAttributes_Example_1"></a>

This example illustrates one usage of DescribeAccountAttributes.

#### Sample Request
<a name="API_DescribeAccountAttributes_Example_1_Request"></a>

```

POST / HTTP/1.1
Host: dms.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256
Credential=<Credential>,
SignedHeaders=contenttype;date;host;user-
agent;x-amz-date;x-amz-target;x-amzn-
requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonDMSv20160101.DescribeAccountAttributes
```

#### Sample Response
<a name="API_DescribeAccountAttributes_Example_1_Response"></a>

```
 HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
   "AccountQuotas":[
      {
         "Max":20,
         "AccountQuotaName":"ReplicationInstances",
         "Used":12
      },
      {
         "Max":10000,
         "AccountQuotaName":"AllocatedStorage",
         "Used":6339
      },
      {
         "Max":20,
         "AccountQuotaName":"ReplicationSubnetGroups",
         "Used":5
      },
      {
         "Max":20,
         "AccountQuotaName":"SubnetsPerReplicationSubnetGroup",
         "Used":4
      },
      {
         "Max":100,
         "AccountQuotaName":"Endpoints",
         "Used":10
      },
      {
         "Max":200,
         "AccountQuotaName":"ReplicationTasks",
         "Used":2
      },
      {
         "Max":20,
         "AccountQuotaName":"EndpointsPerInstance",
         "Used":8
      }
   ]
   "UniqueAccountIdentifier":"c44445555666"
}
```

## See Also
<a name="API_DescribeAccountAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeAccountAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeAccountAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeAccountAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeAccountAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeAccountAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeAccountAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeAccountAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeAccountAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeAccountAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeAccountAttributes)
