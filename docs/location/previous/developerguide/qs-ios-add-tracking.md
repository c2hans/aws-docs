---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/qs-ios-add-tracking.html
---

# Add Amazon Location tracking to your application
<a name="qs-ios-add-tracking"></a>

The last step for your application is to add tracking functionality to your app. In this case, you will add start tracking, stop tracking, fetch and display tracker points on your app.

1. Add the `TrackingBottomView.swift` file in your project. Which has a button that starts and stops tracking user locations and shows tracking points on the map.

   ```
   import SwiftUI

   struct TrackingBottomView: View {
       @ObservedObject var trackingViewModel: TrackingViewModel
       var body: some View {
              Button(action: {
                  Task {
                      if(trackingViewModel.trackingButtonText == NSLocalizedString("StartTrackingLabel", comment: "")) {
                          trackingViewModel.startTracking()
                      } else {
                          trackingViewModel.stopTracking()
                      }
                  }
              }) {
                  HStack {
                      Spacer()
                      Text("Tracking")
                          .foregroundColor(trackingViewModel.trackingButtonColor)
                          .background(.white)
                          .cornerRadius(15.0)

                      Image(systemName: trackingViewModel.trackingButtonIcon)
                          .resizable()
                          .frame(width: 24, height: 24)
                          .padding(5)
                          .background(.white)
                          .foregroundColor(trackingViewModel.trackingButtonColor)

                  }
              }
              .accessibility(identifier: "TrackingButton")
              .background(.white)
              .clipShape(RoundedRectangle(cornerRadius: 8))
              .padding(.trailing, 10)
              .padding(.bottom, 40)
              .frame(width: 130, alignment: .trailing)
              .shadow(color: Color.black.opacity(0.3), radius: 3, x: 0, y: 2)
          }
   }
   ```

1. Update `TrackingView.swift` file with the following code

   ```
   import SwiftUI

   struct TrackingView: View {
       @ObservedObject var trackingViewModel: TrackingViewModel
       var body: some View {
           ZStack(alignment: .bottom) {
               if trackingViewModel.mapSigningIntialised {
                   MapView(trackingViewModel: trackingViewModel)
                   VStack {
                       UserLocationView(trackingViewModel: trackingViewModel)
                       CenterAddressView(trackingViewModel: trackingViewModel)
                       TrackingBottomView(trackingViewModel: trackingViewModel)
                   }
               }
               else {
                   Text("Loading...")
               }
           }
           .onAppear() {
               if !trackingViewModel.identityPoolId.isEmpty {
                   Task {
                       do {
                           try await trackingViewModel.authWithCognito(identityPoolId: trackingViewModel.identityPoolId)
                       }
                       catch {
                           print(error)
                       }
                   }
               }
           }
       }
   }
   ```

1. Add the following code in `TrackingViewModel.swift` file. These functions are responsible for start and stop tracking. It will also show an error alert if user location permission is denied.

1. To implement foreground tracking copy paste the following code example:

   ```
   func showLocationDeniedRationale() {
           alertTitle = NSLocalizedString("locationManagerAlertTitle", comment: "")
           alertMessage = NSLocalizedString("locationManagerAlertText", comment: "")
           showAlert = true
       }

       // Required in info.plist: Privacy - Location When In Use Usage Description
       func startTracking() {
           do {
               print("Tracking Started...")
               if(client == nil) {
                   initializeClient()
               }
               try client.startTracking()
               DispatchQueue.main.async { [self] in
                   self.trackingButtonText = NSLocalizedString("StopTrackingLabel", comment: "")
                   self.trackingButtonColor = .red
                   self.trackingButtonIcon = "pause.circle"
                   trackingActive = true
               }
           } catch TrackingLocationError.permissionDenied {
               showLocationDeniedRationale()
           } catch {
               print("error in tracking")
           }
       }

       func stopTracking() {
           print("Tracking Stopped...")
           client.stopTracking()
           trackingButtonText = NSLocalizedString("StartTrackingLabel", comment: "")
           trackingButtonColor = .blue
           trackingButtonIcon = "play.circle"
           trackingActive = false
       }
   ```
**Note**
The `startTracking` will ask for the user's location permission. The application must use **When In Use** or **Only Once** permissions. Otherwise, the application will throw a permission denied error.

To get and display tracking locations, follow this procedure:

1. To get the locations from the user's device, you need to provide the start and end date and time. A single call returns a maximum of 100 tracking locations, but if there are more than 100 tracking locations, it will return a `nextToken` value. You will need to call subsequent `getTrackerDeviceLocation` calls with `nextToken` to load more tracking points for the given start and end time.

   ```
    func getTrackingPoints(nextToken: String? = nil) async throws {
           guard trackingActive else {
               return
           }
           // Initialize startTime to 24 hours ago from the current date and time.
           let startTime: Date = Date().addingTimeInterval(-86400)
           var endTime: Date = Date()
           if lastGetTrackingTime != nil {
               endTime = lastGetTrackingTime!
           }
           let result = try await client?.getTrackerDeviceLocation(nextToken: nextToken, startTime: startTime, endTime: endTime)
           if let trackingData = result {

               lastGetTrackingTime = Date()
               let devicePositions = trackingData.devicePositions

               let positions = devicePositions!.sorted { (pos1: LocationClientTypes.DevicePosition, pos2: LocationClientTypes.DevicePosition) -> Bool in
                   guard let date1 = pos1.sampleTime,
                         let date2 = pos2.sampleTime else {
                       return false
                   }
                   return date1 < date2
               }

               let trackingPoints = positions.compactMap { position -> CLLocationCoordinate2D? in
                   guard let latitude = position.position!.last, let longitude = position.position!.first else {
                       return nil
                   }
                   return CLLocationCoordinate2D(latitude: latitude, longitude: longitude)
               }
               DispatchQueue.main.async {
                   self.mapViewDelegate!.drawTrackingPoints( trackingPoints: trackingPoints)
               }
               if let nextToken = trackingData.nextToken {
                   try await getTrackingPoints(nextToken: nextToken)
               }
           }
       }
   ```

1. Now replace the code in the `MapView.swift` file with the following code:

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

           func mapView(_ mapView: MLNMapView, viewFor annotation: MLNAnnotation) -> MLNAnnotationView? {
               guard let pointAnnotation = annotation as? MLNPointAnnotation else {
                   return nil
               }

               let reuseIdentifier: String
               var color: UIColor = .black
               if pointAnnotation.accessibilityLabel == "Tracking" {
                   reuseIdentifier = "TrackingAnnotation"
                   color = UIColor(red: 0.00784313725, green: 0.50588235294, blue: 0.58039215686, alpha: 1)
               } else if pointAnnotation.accessibilityLabel == "LocationChange" {
                   reuseIdentifier = "LocationChange"
                   color = .gray
               } else {
                   reuseIdentifier = "DefaultAnnotationView"
               }

               var annotationView = mapView.dequeueReusableAnnotationView(withIdentifier: reuseIdentifier)

               if annotationView == nil {
                   if reuseIdentifier != "DefaultAnnotationView" {
                       annotationView = MLNAnnotationView(annotation: annotation, reuseIdentifier: reuseIdentifier)
                       //If point annotation is an uploaded Tracking point the radius is 20 and color is blue, otherwise radius is 10 and color is gray
                       let radius = pointAnnotation.accessibilityLabel == "Tracking" ? 20:10
                       annotationView?.frame = CGRect(x: 0, y: 0, width: radius, height: radius)
                       annotationView?.backgroundColor = color
                       annotationView?.layer.cornerRadius = 10

                       if pointAnnotation.accessibilityLabel == "Tracking" {
                           annotationView?.layer.borderColor = UIColor.white.cgColor
                           annotationView?.layer.borderWidth = 2.0
                           annotationView?.layer.shadowColor = UIColor.black.cgColor
                           annotationView?.layer.shadowOffset = CGSize(width: 0, height: 2)
                           annotationView?.layer.shadowRadius = 3
                           annotationView?.layer.shadowOpacity = 0.2
                           annotationView?.clipsToBounds = false
                       }
                   }
                   else {
                       return nil
                   }
               }

               return annotationView
           }

           func mapView(_ mapView: MLNMapView, didUpdate userLocation: MLNUserLocation?) {
               if (userLocation?.location) != nil {
                   if trackingViewModel.trackingActive {
                       let point = MLNPointAnnotation()
                       point.coordinate = (userLocation?.location!.coordinate)!
                       point.accessibilityLabel = "LocationChange"
                       mapView.addAnnotation(point)
                       Task {
                           do {
                               try await trackingViewModel.getTrackingPoints()
                           }
                           catch {
                               print(error)
                           }
                       }
                   }
               }
           }

           func checkIfTrackingAnnotationExists(on mapView: MLNMapView, at coordinates: CLLocationCoordinate2D) -> Bool {
               let existingAnnotation = mapView.annotations?.first(where: { annotation in
                   guard let annotation = annotation as? MLNPointAnnotation else { return false }
                   return annotation.coordinate.latitude == coordinates.latitude &&
                   annotation.coordinate.longitude == coordinates.longitude && annotation.accessibilityLabel == "Tracking" })
               return existingAnnotation != nil
           }

           public func drawTrackingPoints(trackingPoints: [CLLocationCoordinate2D]?) {
               guard let mapView = mlnMapView, let newTrackingPoints = trackingPoints, !newTrackingPoints.isEmpty else {
                   return
               }

               let uniqueCoordinates = newTrackingPoints.filter { coordinate in
                   !checkIfTrackingAnnotationExists(on: mapView, at: coordinate)
               }

               let points = uniqueCoordinates.map { coordinate -> MLNPointAnnotation in
                   let point = MLNPointAnnotation()
                   point.coordinate = coordinate
                   point.accessibilityLabel = "Tracking"
                   return point
               }
               mapView.addAnnotations(points)
           }
       }
   }

   protocol MapViewDelegate: AnyObject {
       func drawTrackingPoints(trackingPoints: [CLLocationCoordinate2D]?)
   }
   ```

To localize string values , use the following procedure.

1. Create and add a new file called `Localizable.xcstrings`.

1. Right-click on the `Localizable.xcstrings` file and open it as **Source Code**.

1. Replace its content with the following:

   ```
   {
     "sourceLanguage" : "en",
     "strings" : {
       "Cancel" : {
         "extractionState" : "manual",
         "localizations" : {
           "en" : {
             "stringUnit" : {
               "state" : "translated",
               "value" : "Cancel"
             }
           }
         }
       },
       "Error" : {
         "extractionState" : "manual",
         "localizations" : {
           "en" : {
             "stringUnit" : {
               "state" : "translated",
               "value" : "Error"
             }
           }
         }
       },
       "Loading..." : {

       },
       "locationManagerAlertText" : {
         "extractionState" : "manual",
         "localizations" : {
           "en" : {
             "stringUnit" : {
               "state" : "translated",
               "value" : "Allow \\\"Quick Start App\\\" to use your location"
             }
           }
         }
       },
       "locationManagerAlertTitle" : {
         "extractionState" : "manual",
         "localizations" : {
           "en" : {
             "stringUnit" : {
               "state" : "translated",
               "value" : "We need your location to detect your location in map"
             }
           }
         }
       },
       "NotAllFieldsAreConfigured" : {
         "extractionState" : "manual",
         "localizations" : {
           "en" : {
             "stringUnit" : {
               "state" : "translated",
               "value" : "Not all the fields are configured"
             }
           }
         }
       },
       "OK" : {
         "extractionState" : "manual",
         "localizations" : {
           "en" : {
             "stringUnit" : {
               "state" : "translated",
               "value" : "OK"
             }
           }
         }
       },
       "StartTrackingLabel" : {
         "localizations" : {
           "en" : {
             "stringUnit" : {
               "state" : "translated",
               "value" : "Start Tracking"
             }
           }
         }
       },
       "StopTrackingLabel" : {
         "localizations" : {
           "en" : {
             "stringUnit" : {
               "state" : "translated",
               "value" : "Stop Tracking"
             }
           }
         }
       },
       "Tracking" : {

       }
     },
     "version" : "1.0"
   }
   ```

1. Save your files, and build and run your app to preview the functionality.

1. Allow the location permission and tap on the tracking button. The app will start uploading user locations and upload them to the Amazon Location tracker. It will also show user location changes, tracking points, and current address on the map.

Your quick-start application is complete. This tutorial has shown you how to create an iOS application that:
+ Creates a map that users can interact with.
+ Handles several map events associated with the user changing the map view.
+ Calls an Amazon Location Service API, specifically to search the map at a location, using Amazon Location's searchByPosition API.

## What's next
<a name="qs-ios-whats-next"></a>

You have completed the quick start tutorial, and should have an idea of how Amazon Location Service is used to build applications.

The source code for this application is available on [GitHub](https://github.com/aws-geospatial/amazon-location-samples-ios/tree/main/quick-start).

To get more out of Amazon Location, you can check out the following resources:
+ Dive deeper into the [concepts of Amazon Location Service](how-it-works.md)
+ Get more information about [how to use Amazon Location features and functionality](using-amazon-location.md)
+ See how to expand on this sample and build more complex applications by looking at [code examples using Amazon Location](samples.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
