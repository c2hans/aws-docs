---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_StreamingAccessDetails.html
---

# StreamingAccessDetails
<a name="API_StreamingAccessDetails"></a>

Contains information about an AWS service that has been granted streaming access to your Resource Explorer data.

## Contents
<a name="API_StreamingAccessDetails_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CreatedAt **   <a name="resourceexplorer-Type-StreamingAccessDetails-CreatedAt"></a>
The date and time when streaming access was granted to the AWS service, in ISO 8601 format.
Type: Timestamp
Required: Yes

 ** ServicePrincipal **   <a name="resourceexplorer-Type-StreamingAccessDetails-ServicePrincipal"></a>
The service principal of the AWS service that has streaming access to your Resource Explorer data. A service principal is a unique identifier for an AWS service.
Type: String
Required: Yes

## See Also
<a name="API_StreamingAccessDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/StreamingAccessDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/StreamingAccessDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/StreamingAccessDetails)
