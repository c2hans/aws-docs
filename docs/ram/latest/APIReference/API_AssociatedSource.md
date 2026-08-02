---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_AssociatedSource.html
---

# AssociatedSource
<a name="API_AssociatedSource"></a>

Information about a source association in a resource share. Source associations control which sources can be used with service principals.

## Contents
<a name="API_AssociatedSource_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** creationTime **   <a name="ram-Type-AssociatedSource-creationTime"></a>
The date and time when the source association was created.
Type: Timestamp
Required: No

 ** lastUpdatedTime **   <a name="ram-Type-AssociatedSource-lastUpdatedTime"></a>
The date and time when the source association was last updated.
Type: Timestamp
Required: No

 ** resourceShareArn **   <a name="ram-Type-AssociatedSource-resourceShareArn"></a>
The Amazon Resource Name (ARN) of the resource share that contains the source association.
Type: String
Required: No

 ** sourceId **   <a name="ram-Type-AssociatedSource-sourceId"></a>
The identifier of the source. This can be an account ID, Amazon Resource Name (ARN), organization ID, or organization path.
Type: String
Required: No

 ** sourceType **   <a name="ram-Type-AssociatedSource-sourceType"></a>
The type of source.
Type: String
Required: No

 ** status **   <a name="ram-Type-AssociatedSource-status"></a>
The current status of the source association.
Type: String
Required: No

 ** statusMessage **   <a name="ram-Type-AssociatedSource-statusMessage"></a>
A message about the status of the source association.
Type: String
Required: No

## See Also
<a name="API_AssociatedSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/AssociatedSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/AssociatedSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/AssociatedSource)
