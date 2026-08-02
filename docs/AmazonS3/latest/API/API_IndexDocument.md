---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_IndexDocument.html
---

# IndexDocument
<a name="API_IndexDocument"></a>

Container for the `Suffix` element.

## Contents
<a name="API_IndexDocument_Contents"></a>

 ** Suffix **   <a name="AmazonS3-Type-IndexDocument-Suffix"></a>
A suffix that is appended to a request that is for a directory on the website endpoint. (For example, if the suffix is `index.html` and you make a request to `samplebucket/images/`, the data that is returned will be for the object with the key name `images/index.html`.) The suffix must not be empty and must not include a slash character.
Replacement must be made for object keys containing special characters (such as carriage returns) when using XML requests. For more information, see [ XML related object key constraints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints).
Type: String
Required: Yes

## See Also
<a name="API_IndexDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/IndexDocument)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/IndexDocument)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/IndexDocument)
