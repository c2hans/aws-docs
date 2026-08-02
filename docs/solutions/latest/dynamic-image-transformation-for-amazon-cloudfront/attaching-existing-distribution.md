---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/attaching-existing-distribution.html
---

# Attaching an existing CloudFront distribution
<a name="attaching-existing-distribution"></a>

This section provides instructions for integrating the solution with your existing CloudFront distribution for both architectures.

**Note**
In the following instructions, UUID is used to reference the deployment UUID of your Dynamic Image Transformation for Amazon CloudFront stack. You can find this value by inspecting the Physical ID of a `AWS::CloudFront::Function` deployed in your stack, and extracting the value found after the word `modifier-`.
