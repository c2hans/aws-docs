---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/tutorial-maplibre-ios.html
---

# Using the MapLibre Native SDK for iOS with Amazon Location Service
<a name="tutorial-maplibre-ios"></a>

Use [MapLibre Native SDK for iOS](https://github.com/maplibre/maplibre-gl-native) to embed client-side maps into iOS applications.

The MapLibre Native SDK for iOS is a library based on [Mapbox GL Native](https://github.com/mapbox/mapbox-gl-native), and is compatible with the styles and tiles provided by the Amazon Location Service Maps API. You can integrate MapLibre Native SDK for iOS to embed interactive map views with scalable, customizable vector maps into your iOS applications.

This tutorial describes how to integrate the MapLibre Native SDK for iOS with Amazon Location. The sample application for this tutorial is available as part of the Amazon Location Service samples repository on [GitHub](https://github.com/aws-samples/amazon-location-samples).

## Building the application: Initialization
<a name="tutorial-maplibre-ios-initialization"></a>

To initialize your application:

1. Create a new Xcode project from the **App** template.

1. Select **SwiftUI** for its interface.

1. Select **SwiftUI** application for its Life Cycle.

1. Select **Swift** for its language.

## Adding MapLibre dependencies using Swift Packages
<a name="tutorial-maplibre-add-dependencies"></a>

To add a package dependency to your Xcode project:

1. Navigate to **File** > **Swift Packages** > **Add Package Dependency**.

1. Enter the repository URL: **https://github.com/maplibre/maplibre-gl-native-distribution**
**Note**
For more information about Swift Packages see [Adding Package Dependencies to Your App](https://developer.apple.com/documentation/xcode/adding_package_dependencies_to_your_app) at Apple.com

1. In your terminal, install CocoaPods:

   ```
   sudo gem install cocoapods
   ```

1. Navigate to your application's project directory and initialize the **Podfile** with the CocoaPods package manager:

   ```
   pod init
   ```

1. Open the **Podfile** to add `AWSCore` as a dependency:

   ```
   platform :ios, '12.0'

   target 'Amazon Location Service Demo' do
     use_frameworks!

     pod 'AWSCore'
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
<a name="tutorial-maplibre-ios-configuration"></a>

Add the following keys and values to **Info.plist** to configure the application:

| Key | Value |
| --- | --- |
| AWSRegion | us-east-1 |
| IdentityPoolId | us-east-1:54f2ba88-9390-498d-aaa5-0d97fb7ca3bd |
| MapName | ExampleMap |

## Building the application: ContentView layout
<a name="tutorial-maplibre-ios-contentview-layout"></a>

To render the map, edit `ContentView.swift`:
+  Add a `MapView` which renders the map.
+ Add a `TextField` which displays attribution.

This also sets the map's initial center point.

```
import SwiftUI

struct ContentView: View {
    @State private var attribution = ""

    var body: some View {
        MapView(attribution: $attribution)
            .centerCoordinate(.init(latitude: 49.2819, longitude: -123.1187))
            .zoomLevel(12)
            .edgesIgnoringSafeArea(.all)
            .overlay(
                TextField("", text: $attribution)
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

**Note**
You must provide word mark or text attribution for each data provider that you use, either on your application or your documentation. Attribution strings are included in the style descriptor response under the `sources.esri.attribution`, `sources.here.attribution`, and `source.grabmaptiles.attribution` keys. When using Amazon Location resources with [data providers](https://docs.aws.amazon.com/location/previous/developerguide/what-is-data-provider.html), make sure to read the [service terms and conditions](https://aws.amazon.com/service-terms/).

## Building the application: Request transformation
<a name="tutorial-maplibre-ios-request-transformation"></a>

Create a new Swift file named `AWSSignatureV4Delegate.swift` containing the following class definition to intercept AWS requests and sign them using [Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html). An instance of this class will be assigned as the offline storage delegate, which is also responsible for rewriting URLs, in the map view.

```
import AWSCore
import Mapbox

class AWSSignatureV4Delegate : NSObject, MGLOfflineStorageDelegate {
    private let region: AWSRegionType
    private let identityPoolId: String
    private let credentialsProvider: AWSCredentialsProvider

    init(region: AWSRegionType, identityPoolId: String) {
        self.region = region
        self.identityPoolId = identityPoolId
        self.credentialsProvider = AWSCognitoCredentialsProvider(regionType: region, identityPoolId: identityPoolId)
        super.init()
    }

    class func doubleEncode(path: String) -> String? {
        return path.addingPercentEncoding(withAllowedCharacters: .urlPathAllowed)?
            .addingPercentEncoding(withAllowedCharacters: .urlPathAllowed)
    }

    func offlineStorage(_ storage: MGLOfflineStorage, urlForResourceOf kind: MGLResourceKind, with url: URL) -> URL {
        if url.host?.contains("amazonaws.com") != true {
            // not an AWS URL
            return url
        }

        // URL-encode spaces, etc.
        let keyPath = String(url.path.dropFirst())
        guard let percentEncodedKeyPath = keyPath.addingPercentEncoding(withAllowedCharacters: .urlPathAllowed) else {
            print("Invalid characters in path '\(keyPath)'; unsafe to sign")
            return url
        }

        let endpoint = AWSEndpoint(region: region, serviceName: "geo", url: url)
        let requestHeaders: [String: String] = ["host": endpoint!.hostName]

        // sign the URL
        let task = AWSSignatureV4Signer
            .generateQueryStringForSignatureV4(
                withCredentialProvider: credentialsProvider,
                httpMethod: .GET,
                expireDuration: 60,
                endpoint: endpoint!,
                // workaround for https://github.com/aws-amplify/aws-sdk-ios/issues/3215
                keyPath: AWSSignatureV4Delegate.doubleEncode(path: percentEncodedKeyPath),
                requestHeaders: requestHeaders,
                requestParameters: .none,
                signBody: true)
        task.waitUntilFinished()

        if let error = task.error as NSError? {
            print("Error occurred: \(error)")
        }

        if let result = task.result {
            var urlComponents = URLComponents(url: (result as URL), resolvingAgainstBaseURL: false)!
            // re-use the original path; workaround for https://github.com/aws-amplify/aws-sdk-ios/issues/3215
            urlComponents.path = url.path

            // have Mapbox GL fetch the signed URL
            return (urlComponents.url)!
        }

        // fall back to an unsigned URL
        return url
    }
}
```

## Building the application: Map view
<a name="tutorial-maplibre-ios-request-map-view"></a>

The Map View is responsible for initializing an instance of `AWSSignatureV4Delegate` and configuring the underlying `MGLMapView`, which fetches resources and renders the map. It also handles propagating attribution strings from the style descriptor's source back to the `ContentView`.

Create a new Swift file named `MapView.swift` containing the following `struct` definition:

```
import SwiftUI
import AWSCore
import Mapbox

struct MapView: UIViewRepresentable {
    @Binding var attribution: String

    private var mapView: MGLMapView
    private var signingDelegate: MGLOfflineStorageDelegate

    init(attribution: Binding<String>) {
        let regionName = Bundle.main.object(forInfoDictionaryKey: "AWSRegion") as! String
        let identityPoolId = Bundle.main.object(forInfoDictionaryKey: "IdentityPoolId") as! String
        let mapName = Bundle.main.object(forInfoDictionaryKey: "MapName") as! String

        let region = (regionName as NSString).aws_regionTypeValue()

        // MGLOfflineStorage doesn't take ownership, so this needs to be a member here
        signingDelegate = AWSSignatureV4Delegate(region: region, identityPoolId: identityPoolId)

        // register a delegate that will handle SigV4 signing
        MGLOfflineStorage.shared.delegate = signingDelegate

        mapView = MGLMapView(
            frame: .zero,
            styleURL: URL(string: "https://maps.geo.\(regionName).amazonaws.com/maps/v0/maps/\(mapName)/style-descriptor"))

        _attribution = attribution
    }

    func makeCoordinator() -> Coordinator {
        Coordinator($attribution)
    }

    class Coordinator: NSObject, MGLMapViewDelegate {
        var attribution: Binding<String>

        init(_ attribution: Binding<String>) {
            self.attribution = attribution
        }

        func mapView(_ mapView: MGLMapView, didFinishLoading style: MGLStyle) {
            let source = style.sources.first as? MGLVectorTileSource
            let attribution = source?.attributionInfos.first
            self.attribution.wrappedValue = attribution?.title.string ?? ""
        }
    }

    // MARK: - UIViewRepresentable protocol

    func makeUIView(context: UIViewRepresentableContext<MapView>) -> MGLMapView {
        mapView.delegate = context.coordinator

        mapView.logoView.isHidden = true
        mapView.attributionButton.isHidden = true
        return mapView
    }

    func updateUIView(_ uiView: MGLMapView, context: UIViewRepresentableContext<MapView>) {
    }

    // MARK: - MGLMapView proxy

    func centerCoordinate(_ centerCoordinate: CLLocationCoordinate2D) -> MapView {
        mapView.centerCoordinate = centerCoordinate
        return self
    }

    func zoomLevel(_ zoomLevel: Double) -> MapView {
        mapView.zoomLevel = zoomLevel
        return self
    }
}
```

Running this application displays a full-screen map in the style of your choosing. This sample is available as part of the Amazon Location Service samples repository on [GitHub](https://github.com/aws-samples/amazon-location-samples).
