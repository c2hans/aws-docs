---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/qs-ios-add-map.html
---

# Add an Amazon Location interactive map to your application
<a name="qs-ios-add-map"></a>

You will now add the map control to your application. This tutorial uses MapLibre and the AWS API for managing the map view in the application. The map control itself is part of the [MapLibre GL Native iOS](https://docs.maptiler.com/maplibre-gl-native-ios/) library.

1. Add `MapView.swift` file under the **Views** folder with the following code:

   ```
   import SwiftUI
   import MapLibre

   struct MapView: UIViewRepresentable {
       var onMapViewAvailable: ((MLNMapView) -> Void)?
       var mlnMapView: MLNMapView?
       var trackingViewModel: TrackingViewModel

       func makeCoordinator() -> MapView.Coordinator {
           return Coordinator(self, trackingViewModel: trackingViewModel)
       }

       func makeUIView(context: Context) -> MLNMapView {
           let styleURL = URL(string: "https://maps.geo.\(trackingViewModel.region).amazonaws.com/maps/v0/maps/\(trackingViewModel.mapName)/style-descriptor")
           let mapView = MLNMapView(frame: .zero, styleURL: styleURL)
           mapView.autoresizingMask = [.flexibleWidth, .flexibleHeight]
           mapView.setZoomLevel(15, animated: true)
           mapView.showsUserLocation = true
           mapView.userTrackingMode = .follow
           context.coordinator.mlnMapView = mapView
           mapView.delegate = context.coordinator

           mapView.logoView.isHidden = true
           context.coordinator.addCenterMarker()

           onMapViewAvailable?(mapView)
           trackingViewModel.mlnMapView = mapView
           return mapView
       }

       func updateUIView(_ uiView: MLNMapView, context: Context) {
       }

       class Coordinator: NSObject, MLNMapViewDelegate, MapViewDelegate {
           var control: MapView
           var mlnMapView: MLNMapView?
           var trackingViewModel: TrackingViewModel
           var centerMarker: MLNPointAnnotation?

           public init(_ control: MapView, trackingViewModel: TrackingViewModel) {
               self.control = control
               self.trackingViewModel = trackingViewModel
               super.init()
               self.trackingViewModel.mapViewDelegate = self
           }

           func mapViewDidFinishRenderingMap(_ mapView: MLNMapView, fullyRendered: Bool) {
               if(fullyRendered) {
                   mapView.accessibilityIdentifier = "MapView"
                   mapView.isAccessibilityElement = false
               }
           }

           func addCenterMarker() {
               guard let mlnMapView = mlnMapView else {
                   return
               }

               let centerCoordinate = mlnMapView.centerCoordinate
               let marker = MLNPointAnnotation()
               marker.coordinate = centerCoordinate
               marker.accessibilityLabel = "CenterMarker"
               mlnMapView.addAnnotation(marker)
               centerMarker = marker

               trackingViewModel.reverseGeocodeCenter(centerCoordinate: centerCoordinate, marker: marker)
           }

           func mapView(_ mapView: MLNMapView, regionDidChangeAnimated animated: Bool) {
               if let marker = centerMarker {
                                 DispatchQueue.main.asyncAfter(deadline: .now() + 1.0) {
                       mapView.deselectAnnotation(marker, animated: false)
                       marker.coordinate = mapView.centerCoordinate
                       let centerCoordinate = mapView.centerCoordinate
                       self.trackingViewModel.reverseGeocodeCenter(centerCoordinate: centerCoordinate, marker: marker)
                   }
               }
           }
       }
   }
   ```

1. Add `AWSSignatureV4Delegate` file under the **ViewModel** folder. This file is used to sign with all the MapView http requests to render the map:

   ```
   import MapLibre
   import AmazonLocationiOSAuthSDK

   class AWSSignatureV4Delegate : NSObject, MLNOfflineStorageDelegate {
       private let awsSigner: AWSSigner

       init(credentialsProvider: LocationCredentialsProvider) {
           self.awsSigner = {{DENY LIST ERROR}} , serviceName: "geo")
           super.init()
       }

       func offlineStorage(_ storage: MLNOfflineStorage, urlForResourceOf kind: MLNResourceKind, with url: URL) -> URL {
           if url.host?.contains("amazonaws.com") != true {
               return url
           }
           let signedURL = awsSigner.signURL(url: url, expires: .hours(1))

           return signedURL
       }
   }
   ```

1. Add `UserLocationView.swift` file under **Views** folder. This adds a button which centers the map to the user's location

   ```
   import SwiftUI

   struct UserLocationView: View {
       @ObservedObject var trackingViewModel: TrackingViewModel
       var body: some View {
               Button(action: {
                   trackingViewModel.locateMe()
               }) {
                   Image(systemName: "scope")
                       .resizable()
                       .frame(width: 24, height: 24)
                       .padding(5)
                       .background(Color.white)
                       .foregroundColor(.blue)
                       .clipShape(RoundedRectangle(cornerRadius: 8))
                       .shadow(color: Color.black.opacity(0.3), radius: 3, x: 0, y: 2)
               }
               .accessibility(identifier: "LocateMeButton")
               .padding(.trailing, 10)
               .padding(.bottom, 10)
               .frame(maxWidth: .infinity, alignment: .trailing)
       }
   }
   ```

1. Add the `TrackingView.swift` file with the following code:

   ```
   import SwiftUI

   struct TrackingView: View {
       @ObservedObject var trackingViewModel: TrackingViewModel
       var body: some View {
           ZStack(alignment: .bottom) {
               MapView(trackingViewModel: trackingViewModel)
               VStack {
                   UserLocationView(trackingViewModel: trackingViewModel)
               }
           }
           .onAppear() {
               if !trackingViewModel.identityPoolId.isEmpty {
                   trackingViewModel.authWithCognito(identityPoolId: trackingViewModel.identityPoolId)
               }
           }
       }
   }
   ```

You can now build the application. To run it, you may have to set up a device to emulate it in Xcode or use the app on your device. Use this app to see how the map control behaves. You can pan by dragging on the map and pinch to zoom. On your own, you can change how the map control works to customize it to the needs of your application.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
