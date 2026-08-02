---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/content-security.html
---

# Using a content-security policy with the Amazon Chime SDK client library for JavaScript
<a name="content-security"></a>

Modern web applications use a content security policy to protect users from certain classes of attacks. Applications that use the `VideoFxProcessor` must include the policy directives described in this section. The directives give the Amazon Chime SDK access to the resources it needs at runtime.

**Topics**
+ [Required content security policy directives](#required-csp)
+ [Example content security policy](#example-csp)
+ [Content security policy errors](#csp-errors)
+ [Cross-origin opener content security policy](#cross-origin-policy)

## Required content security policy directives
<a name="required-csp"></a>

You must use the following content security policy directives.
+ For `script-src:` add `blob: https://*.sdkassets.chime.aws` to load video processing code, and `wasm-unsafe-eval` to allow running it.
+ For `script-src-elem:` add `blob:` `https://*.sdkassets.chime.aws` to load video processing code from the source.
+ For `worker-src:` add `blob: https://*.sdkassets.chime.aws` to load worker JavaScript across origins.

If you omit any of these entries, or if you use HTTP headers and `http-equiv` meta tags to specify a policy and inadvertently exclude any of these by intersection, then a background filter will not be able to initialize. The filter appears to be unsupported, or it creates a no-op video frame processor. You will see errors in your browser console such as:

```
Refused to connect to
'https://static.sdkassets.chime.aws/bgblur/workers/worker.js…'
because it violates the document's content security policy.
```

### Required script policy directives
<a name="required-script"></a>

To function, the `VideoFxProcessor` class must load JavaScript classes at runtime from an Amazon content delivery network. These classes use WebGL2 to implement post-processing for video. To allow an application to fetch and run these classes, you must include the following directives:
+ `script-src 'self' blob: https://*.sdkassets.chime.aws`
+ `script-src-elem 'self' blob: https://*.sdkassets.chime.aws`

**Note**
For full support on Safari and Firefox, you must use the `script-src` and `script-src-elem` directives.

### Worker policy directive
<a name="required-worker"></a>

The `VideoFxProcessor` loads JavaScript classes as a blob to run a web worker thread. The thread uses machine learning models to processes video. To grant an application access for fetching and using this worker, include the following directive:

`worker-src 'self' blob: https://*.sdkassets.chime.aws`

### WebAssembly policy
<a name="required-web-assembly"></a>

The `VideoFxProcessor` loads a WebAssembly (WASM) module from the same Amazon-owned content delivery network. In Chrome 95 and later, compiled WASM modules cannot be passed across multiple module boundaries. To allow fetching and instantiating these modules, include `'wasm-unsafe-eval'` in the `script-src` directive.

For more information about the Content Security Policy’s documentation for WebAssembly, refer to [WebAssembly Content Security Policy](https://github.com/WebAssembly/content-security-policy/blob/main/proposals/CSP.md) on GitHub.

### (Optional) Background image policy directive
<a name="optional-directives"></a>

To use a dynamically loaded background image with a background replacement filter, the `VideoFxProcessor` must have access to the image. To do that, include a `connect-src` directive with the domain that hosts the image.

## Example content security policy
<a name="example-csp"></a>

The following example policy allows you to use the `VideoFxProcessor`. The `connect-src` definitions aren't specific to a `VideoFxProcessor`. Instead, they're related to the audio and video from an Amazon Chime SDK meeting.

```
<head>
    <meta http-equiv="Content-Security-Policy"
        content="base-uri 'self';
        connect-src       'self' https://*.chime.aws wss://*.chime.aws https://*.amazonaws.com wss://*.chime.aws https://*.ingest.chime.aws;
        script-src        'self' blob: 'wasm-unsafe-eval' https://*.sdkassets.chime.aws;
        script-src-elem   'self' blob: https://*.sdkassets.chime.aws;
        worker-src        'self' blob: https://*.sdkassets.chime.aws;">
</head>
```

## Content security policy errors
<a name="csp-errors"></a>

If you omit any of the required directives, the `VideoFxProcessor` will not instantiate and will be unsupported. In that case, the following (or similar) error appears in the browser console:

```
Refused to connect to
'https://static.sdkassets.chime.aws/ml_media_fx/otherassets/worker.js'
because it violates the document's content security policy.
```

## Cross-origin opener content security policy
<a name="cross-origin-policy"></a>

To limit memory usage, the module prefers to use a `SharedArrayBuffer` for processing. However, this requires that you carefully configure web security. You must set the following headers when serving your application HTML:

```
Cross-Origin-Opener-Policy: same-origin
Cross-Origin-Embedder-Policy: require-corp
```

The server must set these because they have no meta-tag equivalents. If you don't set these headers, the background filters may use slightly more RAM.

Background filters can be CPU-intensive and GPU-intensive. Some mobile devices and lower-specification laptop or desktop computers may not have the power to run the filters along with multiple video streams.
