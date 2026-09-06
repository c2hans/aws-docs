---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/optimization-by-browser.html
---

# Images aren’t optimized on Safari or Firefox
<a name="optimization-by-browser"></a>

 **Symptoms:**
+ Image size or quality optimization works in Chrome or Edge but appears less precise on Safari or Firefox.

 **Cause:**

Safari and Firefox don’t send Client Hints headers, which provide the most precise viewport and device-pixel-ratio signals. The solution falls back to CloudFront device detection and then to configured defaults for these browsers, so they still receive optimized images, but sizing is based on a device classification rather than an exact viewport measurement.

 **Solutions:**
+ This is expected behavior; optimization still applies, using the best available signal for each browser.
+ No configuration is required for Safari or Firefox sizing. When Client Hints are absent, the solution automatically uses CloudFront device detection (mobile, tablet, or desktop classification) to infer viewport and device-pixel-ratio values, so these browsers still receive breakpoint-appropriate images.
+ The policy-level fallback values (`fallback.dpr`, `fallback.viewportWidth` on your `quality` and `autosize` outputs) are a last-resort tier: they apply only when **no** detection signal is available at all (for example, a client that blocks Client Hints and that CloudFront cannot classify). Set them to match your typical audience so this edge case still resolves to a sensible size, but they are not what handles mainstream Safari or Firefox traffic.
+ Format selection is the exception: because it depends on the `Accept` header rather than the device tiers, set `fallback.format` on your `format` output to control the format served when `auto` cannot determine browser support. For the schema, see the transformation policy schema reference in the developer guide.
