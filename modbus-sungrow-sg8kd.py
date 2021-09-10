read_register = {
  "5003": "daily_power_yield_0.01", # Wh
  "5004": "total_power_yield_100",  # MWh
  "5008": "internal_temp_10",       # C
  "5011": "pv1_voltage_10",         # V
  "5012": "pv1_current_10",         # A
  "5013": "pv2_voltage_10",         # V
  "5014": "pv2_current_10",         # A
  "5017": "total_pv_power",         # W
  "5019": "grid_voltage_10",        # V
  "5022": "inverter_current_10",    # A
  "5031": "total_active_power",     # W
  "5036": "grid_frequency_10"       # Hz
  "5071": "array_insulation_resistance_10",  	# k-ohm XX
  "5113": "daily_operation_time",  				# m XX
  "5128": "monthly_power_yield_0.01",			# Wh XX
  
  "5083": "export_power_overflow",  # W - House Grid Consumption (+ = importing, - = exporting)
  "5084": "export_power_indicator", # W - House Grid Consumption Overflow Indicator
  "5091": "power_meter",            # W - House Overall Consumption

  "5097": "daily_purchased_energy_10", # kW
  "5101": "daily_energy_consumption_0.01", # Wh
  "5103": "total_energy_consumption_10",   # kWh
  
  "5216": "export_power_overflow",  # W - House Grid Consumption (+ = importing, - = exporting) #new read register
  "5217": "export_power_indicator", # W - House Grid Consumption Overflow Indicator				#new read register
  "5218": "power_meter",            # W - House Overall Consumption		
  
}

holding_register = {
  "5000": "year",
  "5001": "month",
  "5002": "day",
  "5003": "hour",
  "5004": "minute",
  "5005": "second"
}

scan = """{
  "read": [
        {
            "start": "5000",
            "range": "100"
        },
        {
            "start": "5100",
            "range": "50"
        }
  ],
  "holding": [
    {
      "start": "4999",
      "range": "10"
    }
  ]
}"""

# Match Modbus registers to pvoutput api fields
# Reference: https://pvoutput.org/help/api_specification.html#add-status-service
pvoutput = {
  "Energy Generation": "daily_power_yield",
  "Power Generation": "total_active_power",
  "Temperature": "internal_temp",
  "Voltage": "grid_voltage"
}
