<?php
// Λίστα καναλιών
$channels = [
    'capitalcyp',
    'rik1cyp',
    'rik2cyp',
    'omegacyp',
    'ant1cyp',
    'alphacy',
    // Πρόσθεσε όσα κανάλια θες
];

// Δημιουργία φακέλου αποθήκευσης
$folder = __DIR__ . '/streams';
if (!file_exists($folder)) {
    mkdir($folder, 0777, true);
}

// Για κάθε κανάλι:
foreach ($channels as $channel) {
    echo "⏳ Επεξεργασία: $channel\n";
    $url = "https://anacon.org/app/chans/cy/{$channel}.php";
    $html = fetch_html($url);

    // Πιάσε το m3u8 URL με token
    preg_match('/(https:\/\/.*?\.m3u8\?wmsAuthSign=[^"]+)/', $html, $matches);
    if (!isset($matches[1])) {
        echo "⚠️ Δεν βρέθηκε stream για: $channel\n";
        continue;
    }

    $m3u8_url = $matches[1];
    $file_path = "{$folder}/{$channel}.m3u";

    // Γράψε σε αρχείο .m3u
    file_put_contents($file_path, "#EXTM3U\n$m3u8_url\n");
    echo "✅ Αποθηκεύτηκε: {$file_path}\n";
}

echo "🎉 Ολοκληρώθηκε.\n";

// Συνάρτηση ανάκτησης HTML
function fetch_html($url) {
    $ch = curl_init($url);
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_ENCODING => 'gzip, deflate',
        CURLOPT_HTTPHEADER => [
            'User-Agent: Mozilla/5.0',
            'Accept: text/html',
            'Accept-Encoding: gzip, deflate',
        ],
    ]);
    $result = curl_exec($ch);
    curl_close($ch);
    return $result;
}
?>
