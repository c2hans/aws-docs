---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/server-side-html-sanitization.html
---

# Server-side sanitization and using custom tags and attributes in responses
<a name="server-side-html-sanitization"></a>

Server-side sanitization is applied to the `alt.html` and `alt.markdown` Q&A response fields to prevent stored cross-site scripting (XSS) attacks. QnABot on AWS uses the [sanitize-html](https://www.npmjs.com/package/sanitize-html) library for this purpose, which allows a subset of HTML tags and attributes by default.

For more information on default allowed HTML tags and attributes, see the [default options](https://www.npmjs.com/package/sanitize-html#default-options) for sanitize-html. In addition to the defaults, QnABot on AWS allows the following:
+  `<img>`, `<details>`, and `<summary>` tags
+ The `style` attribute on `<p>` elements (restricted to `white-space: pre-line`)
+ The `translate` attribute on `<span>` elements

**Important**
Any tags or attributes not in the allowlist will be removed from Q&A responses. If your responses use custom HTML tags or attributes, you must add them to the allowlist in `sanitizeOutput.js`.

## Instructions for adding custom tags/attributes to the allowlist
<a name="instructions-for-adding-custom-tagsattributes-to-the-allowlist"></a>

To add custom tags or attributes to the sanitization allowlist:

1. Download the latest QnABot on AWS source code (v7.3.12 or later) from the GitHub repository (https://github.com/aws-solutions/qnabot-on-aws).

1. Open `source/lambda/es-proxy-layer/lib/sanitizeOutput.js` in the QnABot source code.

1. Locate the `sanitizeParams` object in the `sanitize` function.

1. Add your custom tags to `allowedTags`:

   ```
   allowedTags: sanitizeHtml.defaults.allowedTags.concat([
       'question', 'references', 'chatHistory', 'followUpMessage',
       'details', 'summary', 'img',
       'custom-tag',  // add your custom tags here
   ]),
   ```

1. Add custom attributes to `allowedAttributes` if needed:

   ```
   allowedAttributes: {
       ...sanitizeHtml.defaults.allowedAttributes,
       a: ['href'],
       p: ['style'],
       span: ['translate'],
       'custom-tag': ['src', 'width', 'height'],  // add your custom attributes here
   },
   ```

1. Apply the same changes to `source/website/js/components/designer/sanitizeOutput.js`.

1. Rebuild and redeploy the solution following the instructions in the README.

**Important**
Only add tags and attributes that you have thoroughly reviewed for security implications. Adding unsafe tags or attributes could re-introduce XSS vulnerabilities.
