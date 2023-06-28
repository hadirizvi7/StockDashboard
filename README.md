# Stock CLI Dashboard

![Alt text](images/demo.png)

This Command Line Interface app provides users with relevant metrics regarding stocks/ETFs of interest. The functionality is achieved via a single endpoint from the Yahoo Finance API, which provides market data using ticker symbols as input. The JSON response object is then manipulated for key metrics and stored in Python Objects, which are later used as output to the console. Further updates to the codebase will incorporate a frontend component as well as a more customizable way to configure user requests.

## Configuration

The terminal output is based upon a configuration file (see `src/config_files/settings.cfg` for more details). Users can customize this based on stocks/ETFs of interest. This input file is then parsed in `main.py` and then used as parameters for the corresponding API calls.

## API Usage

The current application uses a free tier of the API, meaning it is limited to 35 calls/day. Anything beyond this limit returns a specialized response that is handled separately in the code. Note that [RapidAPI](https://rapidapi.com/hub) is used to interface with the Yahoo Finance API due to the lightweight setup and support provided.

## Setup

### 1. Download the repository to your Local Device

```bash
git clone https://github.com/hadirizvi7/StockDashboard.git
```

### 2. Install the necessary libraries/dependencies

```bash
pip3 install -r requirements.txt
```

### 3. Startup the App (MacOS/Linux)

```bash
python3 src/main.py
```

Be sure to create a `config.py` in the `src/config_files` subdirectory and initialize the following credentials:

1. API_KEY
2. RAPID_API_KEY
3. RAPID_API_HOST

## Next Steps

1. **Containerization**

While the preliminary work has been done to deploy this application to Docker Hub, the actual process itself is not complete. By packaging the code in this way, we can have users utilize the functionality regardless of software/hardware configuration.

2. **Frontend Component**

This application currently operates within the scope of the CLI, which is not very user friendly. A better approach would be to build a wrapper API on top of this logic and incorporate a web/mobile interface. This way, we can serve users a more intuitive UI that all users can interact with.
