# Data Sources

Date: 18.11.2026

## 1. Energy-Charts API (target: carbon intensity)
- Endpoint: public_power, country = de
- License: CC BY 4.0, attribution: energy-charts.info
- Resolution: 15 minutes (to be aggregated to hourly)
- Timestamps: unix seconds (UTC)
- Columns used as generation: Nuclear, Hydro Run-of-River, Biomass, Fossil brown coal / lignite, Fossil hard coal, Fossil oil, Fossil coal-derived gas, Fossil gas, Geothermal, Hydro water reservoir, Hydro pumped storage (treatment pending), Others, Waste, Wind offshore, Wind onshore, Solar
- Columns excluded and why:
  - Hydro pumped storage consumption: electricity used to fill storage, not production.
  - Cross border electricity trading: electricity traded over the borders, not produced in Germany.
  - Load and Residual load: Load is not known in advance at forecast time, and Residual load is calculated from the same hour's wind and solar production.
  - Renewable share of load , generation: calculated from the same hour's production and usage, so using them as features would leak the answer into the model (data leakage).
- Rate limits: stricter limits were introduced for the public API; I did not find exact numbers, so I will fetch month by month with short pauses.
- Date parameters (start/end) seem to follow German local time, while the returned timestamps are in UTC (the first timestamp for start=2023-04-01 was 31.03.2023 22:00 UTC).

## 2. (features: weather)
- I used Open-Meteo Historical Weather API, hourly data, timezone GMT+0 (UTC).
- Timestamps looks like `2023-04-14T00:00` values are UTC and will be marked as UTC in code.
-  In the API request, I used latitude and longitude as a 51.5 and 10.5 (Germany location) but API used closest grid like 51.4938 N, 10.4348 E, 309 m elevation. Moreover for timezone I used GMT+0. I am using 4 different Variables like;
- Temperature (Celsius)
- Wind Speed(100 m)(km/h) , I used 100 m because it is mainly about wind turbines. 
- Cloud Cover Total(%) , It is related to sun.
- Shortwave Solar Radiation GHI(W/m square).
  - Radiation is the average of the preceding hour, other variables are instantaneous values.
## 3. Date range decision
- Start: 16.04.2023
- Reason: last nuclear plants shut down on 15.04.2023, permanent change in the grid mix
- Evidence from data: last nuclear value 50.6 MW, then null; all other columns stayed filled (observed in the 14-17 April 2023 sample).
- Official source: BASE, Nuclear phase-out, accessed 18.11.2026, https://www.base.bund.de/en/nuclear-safety/nuclear-phase-out/nuclear-phase-out_content.html
- Why not earlier: the 2022 energy crisis was mainly caused by the war in Ukraine and Russia's cut in gas supply to Europe, which made that year unusual for the German grid. In addition, nuclear plants were still running then, so earlier data describes a different grid mix.
- End: 31.10.2026

## 4. Open questions
- How to treat null values in other columns
- Meaning of the sign in "Cross border electricity trading"
- Pumped storage treatment
- Load: the real measured load is not known at forecast time. A day ahead load forecast could be used as a feature instead. To be decided.
- Emission factor and type?
- Is there a 1 hour shift between radiatiın and generation timestamps?
- Does Historical API covers 16 APR 2023?
