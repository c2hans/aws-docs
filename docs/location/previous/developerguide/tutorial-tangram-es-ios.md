---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/tutorial-tangram-es-ios.html
---

# Using Tangram ES for iOS with Amazon Location Service
<a name="tutorial-tangram-es-ios"></a>

[Tangram ES](https://github.com/tangrams/tangram-es) is a C\+\+ library for rendering 2D and 3D maps from vector data using OpenGL ES. It's the native counterpart to [Tangram](https://github.com/tangrams/tangram).

Tangram styles built to work with the [Tilezen schema](https://tilezen.readthedocs.io/en/latest/layers/) are largely compatible with Amazon Location when using maps from HERE. These include:
+ [Bubble Wrap](https://github.com/tangrams/bubble-wrap) – A full-featured wayfinding style with helpful icons for points of interest
+ [Cinnabar](https://github.com/tangrams/cinnabar-style) – A classic look and go-to for general mapping applications
+ [Refill ](https://github.com/tangrams/refill-style)– A minimalist map style designed for data visualization overlays, inspired by the seminal Toner style by Stamen Design
+ [Tron](https://github.com/tangrams/tron-style) – An exploration of scale transformations in the visual language of TRON
+ [Walkabout](https://github.com/tangrams/walkabout-style) – An outdoor-focused style that's perfect for hiking or getting out and about

This guide describes how to integrate Tangram ES for iOS with Amazon Location using the Tangram style called Cinnabar. This sample is available as part of the Amazon Location Service samples repository on [GitHub](https://github.com/aws-samples/amazon-location-samples).

While other Tangram styles are best accompanied by raster tiles, which encode terrain information, this feature isn't yet supported by Amazon Location.

**Important**
The Tangram styles in the following tutorial are only compatible with Amazon Location map resources configured with the `VectorHereContrast` style.

## Building the application: Initialization
<a name="tutorial-tangram-es-ios-initialization"></a>

To initialize the application:

1. Create a new Xcode project from the **App** template.

1. Select **SwiftUI** for its interface.

1. Select **SwiftUI** application for its Life Cycle.

1. Select **Swift** for its language.

## Building the application: Add dependencies
<a name="tutorial-tangram-es-ios-add-dependencies"></a>

To add dependencies, you can use a dependency manager, such as [CocoaPods](https://cocoapods.org/):

1. In your terminal, install CocoaPods:

   ```
   sudo gem install cocoapods
   ```

1. Navigate to your application's project directory and initialize the **Podfile** with the CocoaPods package manager:

   ```
   pod init
   ```

1. Open the **Podfile** to add `AWSCore` and `Tangram-es` as dependencies:

   ```
   platform :ios, '12.0'

   target 'Amazon Location Service Demo' do
     use_frameworks!

     pod 'AWSCore'
     pod 'Tangram-es'
   end
   ```

1. Download and install dependencies:

   ```
   pod install --repo-update
   ```

1. Open the Xcode workspace that CocoaPods created:

   ```
   xed .
   ```

## Building the application: Configuration
<a name="tutorial-tangram-es-ios-configuration"></a>

Add the following keys and values to **Info.plist** to configure the application and disable telemetry:

| Key | Value |
| --- | --- |
| AWSRegion | us-east-1 |
| IdentityPoolId | us-east-1:54f2ba88-9390-498d-aaa5-0d97fb7ca3bd |
| MapName | ExampleMap |
| SceneURL | https://www.nextzen.org/carto/cinnabar-style/9/cinnabar-style.zip |

## Building the application: ContentView layout
<a name="tutorial-tangram-es-ios-activity-layout"></a>

To render the map, edit `ContentView.swift`:
+  Add a `MapView` which renders the map.
+ Add a `TextField` which displays attribution.

This also sets the map's initial center point.

**Note**
You must provide word mark or text attribution for each data provider that you use, either on your application or your documentation. Attribution strings are included in the style descriptor response under the `sources.esri.attribution`, `sources.here.attribution`, and `source.grabmaptiles.attribution` keys. When using Amazon Location resources with [data providers](https://docs.aws.amazon.com/location/previous/developerguide/what-is-data-provider.html), make sure to read the [service terms and conditions](https://aws.amazon.com/service-terms/).

```
import SwiftUI
import TangramMap

struct ContentView: View {
    var body: some View {
        MapView()
            .cameraPosition(TGCameraPosition(
                                center: CLLocationCoordinate2DMake(49.2819, -123.1187),
                                zoom: 10,
                                bearing: 0,
                                pitch: 0))
            .edgesIgnoringSafeArea(.all)
            .overlay(
                Text("© 2020 HERE")
                    .disabled(true)
                    .font(.system(size: 12, weight: .light, design: .default))
                    .foregroundColor(.black)
                    .background(Color.init(Color.RGBColorSpace.sRGB, white: 0.5, opacity: 0.5))
                    .cornerRadius(1),
                alignment: .bottomTrailing)
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
```

## Building the application: Request transformation
<a name="tutorial-tangram-es-ios-request-transformation"></a>

Create a new Swift file named `AWSSignatureV4URLHandler.swift` containing the following class definition to intercept AWS requests and sign them using [Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html). This will be registered as a URL handler within the Tangram `MapView`.

```
import AWSCore
import TangramMap

class AWSSignatureV4URLHandler: TGDefaultURLHandler {
    private let region: AWSRegionType
    private let identityPoolId: String
    private let credentialsProvider: AWSCredentialsProvider

    init(region: AWSRegionType, identityPoolId: String) {
        self.region = region
        self.identityPoolId = identityPoolId
        self.credentialsProvider = AWSCognitoCredentialsProvider(regionType: region, identityPoolId: identityPoolId)
        super.init()
    }

    override func downloadRequestAsync(_ url: URL, completionHandler: @escaping TGDownloadCompletionHandler) -> UInt {
        if url.host?.contains("amazonaws.com") != true {
            // not an AWS URL
            return super.downloadRequestAsync(url, completionHandler: completionHandler)
        }

        // URL-encode spaces, etc.
        let keyPath = String(url.path.dropFirst())
        guard let keyPathSafe = keyPath.addingPercentEncoding(withAllowedCharacters: .urlPathAllowed) else {
            print("Invalid characters in path '\(keyPath)'; unsafe to sign")
            return super.downloadRequestAsync(url, completionHandler: completionHandler)
        }

        // sign the URL
        let endpoint = AWSEndpoint(region: region, serviceName: "geo", url: url)
        let requestHeaders: [String: String] = ["host": endpoint!.hostName]
        let task = AWSSignatureV4Signer
            .generateQueryStringForSignatureV4(
                withCredentialProvider: credentialsProvider,
                httpMethod: .GET,
                expireDuration: 60,
                endpoint: endpoint!,
                keyPath: keyPathSafe,
                requestHeaders: requestHeaders,
                requestParameters: .none,
                signBody: true)
        task.waitUntilFinished()

        if let error = task.error as NSError? {
            print("Error occurred: \(error)")
        }

        if let result = task.result {
            // have Tangram fetch the signed URL
            return super.downloadRequestAsync(result as URL, completionHandler: completionHandler)
        }

        // fall back to an unsigned URL
        return super.downloadRequestAsync(url, completionHandler: completionHandler)
    }
}
```

## Building the application: Map view
<a name="tutorial-tangram-es-ios-request-main-activity"></a>

The map view is responsible for initializing an instance of `AWSSignatureV4Delegate` and configuring the underlying `MGLMapView`, which fetches resources and renders the map. It also handles propagating attribution strings from the style descriptor's source back to the `ContentView`.

Create a new Swift file named `MapView.swift` containing the following `struct` definition:

```
import AWSCore
import TangramMap
import SwiftUI

struct MapView: UIViewRepresentable {
    private let mapView: TGMapView

    init() {
        let regionName = Bundle.main.object(forInfoDictionaryKey: "AWSRegion") as! String
        let identityPoolId = Bundle.main.object(forInfoDictionaryKey: "IdentityPoolId") as! String
        let mapName = Bundle.main.object(forInfoDictionaryKey: "MapName") as! String
        let sceneURL = URL(string: Bundle.main.object(forInfoDictionaryKey: "SceneURL") as! String)!

        let region = (regionName as NSString).aws_regionTypeValue()

        // rewrite tile URLs to point at AWS resources
        let sceneUpdates = [
            TGSceneUpdate(path: "sources.mapzen.url",
                          value: "https://maps.geo.\(regionName).amazonaws.com/maps/v0/maps/\(mapName)/tiles/{z}/{x}/{y}")]

        // instantiate a TGURLHandler that will sign AWS requests
        let urlHandler = AWSSignatureV4URLHandler(region: region, identityPoolId: identityPoolId)

        // instantiate the map view and attach the URL handler
        mapView = TGMapView(frame: .zero, urlHandler: urlHandler)

        // load the map style and apply scene updates (properties modified at runtime)
        mapView.loadScene(from: sceneURL, with: sceneUpdates)
    }

    func cameraPosition(_ cameraPosition: TGCameraPosition) -> MapView {
        mapView.cameraPosition = cameraPosition

        return self
    }

    // MARK: - UIViewRepresentable protocol

    func makeUIView(context: Context) -> TGMapView {
        return mapView
    }

    func updateUIView(_ uiView: TGMapView, context: Context) {
    }
}
```

Running this application displays a full-screen map in the style of your choosing. This sample is available as part of the Amazon Location Service samples repository on [GitHub](https://github.com/aws-samples/amazon-location-samples).
