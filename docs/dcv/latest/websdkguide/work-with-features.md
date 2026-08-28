---
source_url: https://docs.aws.amazon.com/dcv/latest/websdkguide/work-with-features.html
---

# Work with Amazon DCV features
<a name="work-with-features"></a>

The availability of Amazon DCV features depends on the permissions configured for the Amazon DCV session and the capabilities of the client's web browser.

 The features that are available in a Amazon DCV session are managed by the permissions that have been specified for the session. This means that even if a feature is supported by the Amazon DCV Web Client SDK, access to that feature might be prevented based on the permissions defined by the session administrator. For more information, see [ Configuring Amazon DCV Authorization](https://docs.aws.amazon.com/dcv/latest/adminguide/security-authorization.html) in the *Amazon DCV Administrator Guide* .

## Understanding the featuresUpdate callback function
<a name="understand"></a>

 When the availability of a feature in a Amazon DCV session changes, the Amazon DCV Web Client SDK notifies you using the `featuresUpdate` callback function that you specify at the time of establishing the connection. For example:

```
featuresUpdate: function (connection, list) {
  {{...}}
},
```

 The callback function notifies you only of the features for which the availability has changed. The `list` parameter is an array of strings, and it includes only the names of the updated features. For example, if the availability of the audio input feature changes for the session, the parameter includes only `["audio-in"]` . If at a later point, the availability of the clipboard copy and paste features change for the session, the parameter includes only `["clipboard-copy", "clipboard-paste"]` .

## Handling feature updates
<a name="handle"></a>

 The `featuresUpdate` callback function only notifies you that the availability of one or more features has changed. To know which features were updated, you must query the feature using the `connection.queryFeature` method. This can be done at any time after the notification of change has been received. This method returns a `Promise` that resolves to the requested feature's updated status. The `status` value is always associated and it has a Boolean ( `true` \| `false` ) property called `enabled` . Some features might have additional properties in the `status` value. If the feature's availability has not been updated, it's rejected.

The following example code shows how to do this.

```
// Connection callback called
function featuresUpdate (_, list) {
  if (list.length > 0) {
    list.forEach((feat) => {
      connection.queryFeature(feat).then(status => console.log(feat, "is", status.enabled)));
    });
  }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
