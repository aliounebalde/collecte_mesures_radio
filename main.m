data = jsondecode(fileread('results.json'));

distances = [data.measurements.distance_m];
rssi = [data.measurements.rssi_dBm];
throughput = [data.measurements.throughput_Mbps];
latency = [data.measurements.latency_ms];

plot(distances , rssi)