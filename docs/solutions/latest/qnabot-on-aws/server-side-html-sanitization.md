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
Any tags or attributes not in the allowlist will be removed from Q&A responses. If your responses use custom HTML tags or attributes, you must add them to the allowlist in `source/bin/sanitizeAllowlist.js`.

## Instructions for adding custom tags/attributes to the allowlist
<a name="instructions-for-adding-custom-tagsattributes-to-the-allowlist"></a>

QnABot on AWS maintains a single, canonical allowlist configuration file, `source/bin/sanitizeAllowlist.js`. A build-time script automatically generates two runtime copies from this single file: one for the Fulfillment Lambda (`source/lambda/es-proxy-layer/lib/sanitizeOutput.js`) and one for the Content Designer (`source/website/js/components/designer/sanitizeOutput.js`). Both copies stay in sync. Do not edit the generated `sanitizeOutput.js` files directly—they are overwritten on every build. For more information, see [source/bin/README.md](https://github.com/aws-solutions/qnabot-on-aws/blob/main/source/bin/README.md) in the GitHub repository.

To add custom tags or attributes to the sanitization allowlist:

1. Download the latest QnABot on AWS source code (v7.4.4 or later) from the GitHub repository (https://github.com/aws-solutions/qnabot-on-aws).

1. Open `source/bin/sanitizeAllowlist.js` in the QnABot source code.

1. Add your custom tags to `extraAllowedTags`:

   ```
   extraAllowedTags: [
       'question', 'references', 'chatHistory', 'followUpMessage',
       'details', 'summary', 'img',
       'custom-tag',  // add your custom tags here
   ],
   ```

1. Add custom attributes to `extraAllowedAttributes` if needed:

   ```
   extraAllowedAttributes: {
       a: ['href'],
       p: ['style'],
       span: ['translate', 'style'],
       'custom-tag': ['src', 'width', 'height'],  // add your custom attributes here
   },
   ```

1. Rebuild and redeploy the guidance following the instructions in the [README](https://github.com/aws-solutions/qnabot-on-aws/blob/main/README.md) in the GitHub repository. The allowlist sync runs automatically as part of the build (for example, `npm run up` or `update`, or `build-s3-dist.sh`). You do not need to regenerate the two `sanitizeOutput.js` files manually.

**Important**
Only add tags and attributes that you have thoroughly reviewed for security implications. Adding unsafe tags or attributes could re-introduce XSS vulnerabilities.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for QnABot on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
