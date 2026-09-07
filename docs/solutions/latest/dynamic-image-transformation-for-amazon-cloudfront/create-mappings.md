---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/create-mappings.html
---

# Create mappings
<a name="create-mappings"></a>

A mapping connects incoming requests to a specific origin and, optionally, a transformation policy. Each mapping matches requests by **either** a path pattern **or** a host header pattern; you provide exactly one of the two, not both.

 **Navigation:** In the Admin UI left navigation, select **Mappings**, and then choose **Create mapping**.

Provide the following fields:
+  **Name**: A unique name for the mapping, 1-100 characters, using letters, numbers, spaces, underscores, or hyphens.
+  **Description (optional)**: A description of the mapping.
+  **Origin**: Select an origin you created earlier.
+  **Host header pattern**: A pattern matched against the request’s `Host` header, such as `images.example.com` or `*.example.com`. Provide this **or** a path pattern.
+  **Path pattern**: A pattern matched against the request path, such as `/products` or `/products/*` (a trailing `/*` matches everything under the prefix). Provide this **or** a host header pattern.
+  **Transformation Policy (optional)**: Select a transformation policy to apply to matching requests. If you omit it, the default policy (if one is set) applies.

After completing the fields, choose **Save** to create the mapping.

**Example: path-based mapping**

| Field | Value |
| --- | --- |
| Name |  `Product image route`  |
| Origin |  `Product images bucket`  |
| Path pattern |  `/products/*`  |
| Transformation Policy (optional) |  `Optimization policy`  |

**Example: host-header mapping**

| Field | Value |
| --- | --- |
| Name |  `Marketing host route`  |
| Origin |  `Marketing CDN origin`  |
| Host header pattern |  `images.example.com`  |
| Transformation Policy (optional) |  *(none; default policy applies)*  |

 **How a request is matched.** When a request arrives, the solution resolves it to a single mapping using the following precedence:

1.  **Host header mappings are evaluated first.** If the request’s `Host` header matches a host header pattern, that mapping is used.

1.  **Path mappings are evaluated next.** If no host mapping matches, the request path is matched against path patterns, and the **most specific** (longest matching prefix) mapping wins. For example, a request for `/products/shoes/01.jpg` matches a `/products/shoes/*` mapping in preference to a broader `/products/*` mapping.

If no mapping matches, the request returns an error rather than being served.

 **Screenshot of the Create mapping form in the Admin UI.**

![Admin UI Create mapping form](https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/images/admin-ui-create-mapping.png)
