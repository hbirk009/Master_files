import sys

addr = ["fw_version",
"adc_value",
"pt100_reading",
"temperature_limit",
"dac_value",
"pwell_voltage_mcu",
"dvdd_current_threshold1",
"dvdd_current_threshold2",
"dvdd_voltage",
"dvdd_current",
"avdd_current_threshold1",
"avdd_current_threshold2",
"avdd_voltage",
"avdd_current",
"pwell_current_threshold1",
"pwell_current_threshold2",
"pwell_voltage",
"pwell_current",
"enable_signals",
"string_current_value1",
"string_current_value2",
"string_current_value3",
"string_current_value4",
"string_current_value5",
"string_current_value6",
"string_current_value7",
"string_current_value8",
"string_current_value9",
"string_current_value10",
"string_current_value11",
"string_current_value12",
"ctrl_A",
"ctrl_B",
"ctrl_C",
"error_count",
"error_msg"]

volt_not_volt = [1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
for i in range (len(addr)):
  if volt_not_volt[i]:
    print("## get function for "+addr[i] +" in microcontroller")
    print ("def get_"+addr[i]+"(layer, self):")
    print("  data=self.get_register_value(layer, address, self)")
    print("  step_data = data * self.step_voltage")
    print("  return step_data")
    print("\n")
    print("\n")
    print("## set function for "+addr[i] +" in microcontroller")
    print("def set_"+addr[i]+"(layer, voltage, broadcast, self):")
    print("  step_data = round(voltage / step_voltage)")
    print("  self.set_register_value(layer, step_data, broadcast, self)")
    print("\n")
    print("\n")

  elif not volt_not_volt[i]:
    print("## get function for "+addr[i] +" in microcontroller")
    print ("def get_"+addr[i]+"(layer, self):")
    print("  data=self.get_register_value(layer, address, self)")
    print("  step_data = (data * self.step_voltage)/self.shunt")
    print("  return step_data")
    print("\n")
    print("\n")
    print("## set function for "+addr[i] +" in microcontroller")
    print("def set_"+addr[i]+"(layer, current, broadcast, self):")
    print("  step_data = round(self.shunt*current / step_voltage)")
    print("  self.set_register_value(layer, step_data, broadcast, self)")
    print("\n")
    print("\n")
  


