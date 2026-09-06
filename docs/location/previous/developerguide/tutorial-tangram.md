---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/tutorial-tangram.html
---

# Tutorial: using Tangram with Amazon Location Service
<a name="tutorial-tangram"></a>

This section provides the following tutorials on how to integrate Tangram with Amazon Location.

**Important**
The Tangram styles in the following tutorials are only compatible with Amazon Location map resources configured with the `VectorHereContrast` style.

The following is an example of an AWS CLI command to create a new map resource called {{TangramExampleMap}} using the {{VectorHereContrast}} style:

```
aws --region us-east-1 \
  location \
  create-map \
  --map-name "{{TangramExampleMap}}" \
  --configuration "Style={{VectorHereContrast}}"
```

**Note**
Billing is determined by your usage. You may incur fees for the use of other AWS services. For more information, see [Amazon Location Service pricing](https://aws.amazon.com/location/pricing/).

**Topics**
+ [Using Tangram with Amazon Location Service](tutorial-tangram-js.md)
+ [Using Tangram ES for Android with Amazon Location Service](tutorial-tangram-es-android.md)
+ [Using Tangram ES for iOS with Amazon Location Service](tutorial-tangram-es-ios.md)
