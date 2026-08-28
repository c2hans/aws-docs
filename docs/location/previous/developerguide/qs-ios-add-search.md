---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/qs-ios-add-search.html
---

# Add Amazon Location search to your application
<a name="qs-ios-add-search"></a>

 You now will add reverse geocoding search to the application, where you find the items at a location. To simplify the use of an iOS app, we will search the center of the screen. To find a new location, move the map to where you want to search. We will place a marker at the center of the map to show where we are searching.

1. Add the following code in `TrackingViewModel.swift` file which is related to the reverse geocoding search

   ```
   func reverseGeocodeCenter(centerCoordinate: CLLocationCoordinate2D, marker: MLNPointAnnotation) {
       let position = [NSNumber(value: centerCoordinate.longitude), NSNumber(value: centerCoordinate.latitude)]
       searchPositionAPI(position: position, marker: marker)
   }

   func searchPositionAPI(position: [Double], marker: MLNPointAnnotation) {
       if let amazonClient = authHelper.getLocationClient() {
           Task {
               let searchRequest = SearchPlaceIndexForPositionInput(indexName: indexName, language: "en" , maxResults: 10, position: position)
               let searchResponse = try? await amazonClient.searchPosition(indexName: indexName, input: searchRequest)
               DispatchQueue.main.async {
                   self.centerLabel = searchResponse?.results?.first?.place?.label ?? ""
                   self.mlnMapView?.selectAnnotation(marker, animated: true, completionHandler: {})
               }
           }
       }
   }
   ```

1. Update `TrackingView.swift` file with the following code which will show the mapview's centered location's address

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
