---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_Layer.html
---

# Layer
<a name="API_Layer"></a>

An object representing an Amazon ECR image layer.

## Contents
<a name="API_Layer_Contents"></a>

 ** layerAvailability **   <a name="ECR-Type-Layer-layerAvailability"></a>
The availability status of the image layer.
Type: String
Valid Values: `AVAILABLE | UNAVAILABLE | ARCHIVED`
Required: No

 ** layerDigest **   <a name="ECR-Type-Layer-layerDigest"></a>
The `sha256` digest of the image layer.
Type: String
Pattern: `[a-zA-Z0-9-_+.]+:[a-fA-F0-9]+`
Required: No

 ** layerSize **   <a name="ECR-Type-Layer-layerSize"></a>
The size, in bytes, of the image layer.
Type: Long
Required: No

 ** mediaType **   <a name="ECR-Type-Layer-mediaType"></a>
The media type of the layer, such as `application/vnd.docker.image.rootfs.diff.tar.gzip` or `application/vnd.oci.image.layer.v1.tar+gzip`.
Type: String
Required: No

## See Also
<a name="API_Layer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/Layer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/Layer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/Layer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
