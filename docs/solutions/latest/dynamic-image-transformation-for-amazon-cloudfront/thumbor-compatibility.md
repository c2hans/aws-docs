---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/thumbor-compatibility.html
---

# Thumbor compatibility
<a name="thumbor-compatibility"></a>

You can specify Thumbor image requests as you normally would, with filters and other relevant properties added on as suffixes to the default CloudFront **ApiEndpoint**. For more information about using Thumbor, see [List of supported Thumbor filters](use-supported-thumbor-filters.md).

**Note**
Dynamic Image Transformation for Amazon CloudFront includes a Thumbor-style interface in the API; however, those requests are mapped to comparable Sharp library calls, and might not include all available Thumbor filters. For more information about available Thumbor-style filters, see [List of supported Thumbor filters](use-supported-thumbor-filters.md).
