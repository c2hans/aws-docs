---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/qs-ios-create-app-initial-code.html
---

# Set up the initial code for Amazon Location
<a name="qs-ios-create-app-initial-code"></a>

This page provides the initial code for a sample iOS application that integrates with the Amazon Location Service. With this code as a starting point, you can build location-aware iOS apps leveraging features like maps, geocoding, geofencing, tracking, and routing.

**Enable Location permissions in your app**

1. Open your Xcode project.

1. Locate the project's `Info.plist` file.

1. Add the necessary keys for location permissions based on your app's requirements. Here are the keys:
   + `NSLocationWhenInUseUsageDescription`: Description of why your app needs location access when it's in use.
   + `NSLocationAlwaysAndWhenInUseUsageDescription`: Description of why your app needs continuous location access.

Now you will need to configure resource values in your app. Add a new file named `Config.xcconfig` and fill out the values that you had created previously in the Amazon console.

```
REGION =
INDEX_NAME =
MAP_NAME =
IDENTITY_POOL_ID =
TRACKER_NAME =
```

1. From the left side navigator section, select the project.

1. Under the targets section, select your app and click on the info tab.

1. Add info properties with values like the below:

1. Add the `Config.swift` file with the contents below, which will read config values from the Bundle info file.

   ```
   import Foundation

   enum Config {
       static let region = Bundle.main.object(forInfoDictionaryKey: "Region") as! String
       static let mapName = Bundle.main.object(forInfoDictionaryKey: "MapName") as! String
       static let indexName = Bundle.main.object(forInfoDictionaryKey: "IndexName") as! String
       static let identityPoolId = Bundle.main.object(forInfoDictionaryKey: "IdentityPoolId") as! String
       static let trackerName = Bundle.main.object(forInfoDictionaryKey: "TrackerName") as! String
   }
   ```

1. Create a new folder with the name `ViewModel` and add a `TrackingViewModel.swift` file inside it.

   ```
   import SwiftUI
   import AmazonLocationiOSAuthSDK
   import MapLibre

   final class TrackingViewModel : ObservableObject {
       @Published var trackingButtonText = NSLocalizedString("StartTrackingLabel", comment: "")
       @Published var trackingButtonColor = Color.blue
       @Published var trackingButtonIcon = "play.circle"
       @Published var region : String
       @Published var mapName : String
       @Published var indexName : String
       @Published var identityPoolId : String
       @Published var trackerName : String
       @Published var showAlert = false
       @Published var alertTitle = ""
       @Published var alertMessage = ""
       @Published var centerLabel = ""

       var clientIntialised: Bool
       var client: LocationTracker!
       var authHelper: AuthHelper
       var credentialsProvider: LocationCredentialsProvider?
       var mlnMapView: MLNMapView?
       var mapViewDelegate: MapViewDelegate?
       var lastGetTrackingTime: Date?
       var trackingActive: Bool

       init(region: String, mapName: String, indexName: String, identityPoolId: String, trackerName: String) {
           self.region = region
           self.mapName = mapName
           self.indexName = indexName
           self.identityPoolId = identityPoolId
           self.trackerName = trackerName
           self.authHelper = AuthHelper()
           self.trackingActive = false
           self.clientIntialised = false
       }

       func authWithCognito(identityPoolId: String?) {
           guard let identityPoolId = identityPoolId?.trimmingCharacters(in: .whitespacesAndNewlines)
           else {
               alertTitle = NSLocalizedString("Error", comment: "")
               alertMessage = NSLocalizedString("NotAllFieldsAreConfigured", comment: "")
               showAlert = true
               return
           }
           credentialsProvider = authHelper.authenticateWithCognitoUserPool(identityPoolId: identityPoolId)
           initializeClient()
       }

       func initializeClient() {
           client = LocationTracker(provider: credentialsProvider!, trackerName: trackerName)
           clientIntialised = true
       }
   }
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
