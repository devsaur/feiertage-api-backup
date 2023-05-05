# 🎉 Deutsche Feiertage API Backup 🎉

**Hinweis: Dieses Repository ist nicht vom offiziellen Eigentümer der [Feiertage-API](https://feiertage-api.de) erstellt und wird auch nicht von diesem betrieben. Dieses Repository dient lediglich als Backup der Daten, falls die originale Seite nicht verfügbar ist.**

## 📖 Über

Dieses Repository enthält ein Backup der deutschen Feiertage von 2010 bis zum aktuellen Jahr + 10 Jahre in der Zukunft. Die Daten stammen von der [Feiertage-API](https://feiertage-api.de) und werden als rohe JSON-Dateien gespeichert. Das Backup wird durch eine [GitHub Actions-Konfiguration](.github/workflows/fetch_holidays.yml) automatisch aktualisiert und kann bei Bedarf per GitHub Pages bereitgestellt werden.

## 💻 Verwendung der bereitgestellten JSON-Dateien

Sobald die JSON-Dateien über GitHub Pages bereitgestellt sind, können Sie direkt auf sie zugreifen und sie in Ihren Anwendungen oder Projekten verwenden. Die JSON-Dateien sind unter folgender URL-Struktur verfügbar:

```
https://devsaur.github.io/feiertage-api-backup/holidays/holidays_<Jahr>.json
```

Ersetzen Sie `<Jahr>` durch das gewünschte Jahr, um die Feiertage für dieses Jahr abzurufen. Zum Beispiel, um die Feiertage für das Jahr 2022 abzurufen, verwenden Sie die folgende URL:

```
https://devsaur.github.io/feiertage-api-backup/holidays/holidays_2022.json
```

Sie können die JSON-Dateien in Ihren Anwendungen abrufen und verarbeiten, indem Sie HTTP-Anfragen an die entsprechende URL senden. Hier ist ein Beispiel, wie Sie dies in JavaScript tun können:

```javascript
const getHolidays = async (year) => {
  try {
    const response = await fetch(`https://devsaur.github.io/feiertage-api-backup/holidays/holidays_${year}.json`);
    if (response.ok) {
      const holidays = await response.json();
      console.log(holidays);
    } else {
      console.error('Fehler beim Abrufen der Feiertage');
    }
  } catch (error) {
    console.error('Fehler beim Abrufen der Feiertage:', error);
  }
};

getHolidays(2022);
```

Ersetzen Sie `2022` durch das gewünschte Jahr, um die Feiertage für dieses Jahr abzurufen.

## ℹ️ Haftungsausschluss

Obwohl wir uns bemühen, die Daten in diesem Repository so aktuell und korrekt wie möglich zu halten, können wir keine Garantie für die Richtigkeit und Vollständigkeit der Daten übernehmen. Bitte beziehen Sie sich auf die [offizielle Feiertage-API](https://feiertage-api.de) für die aktuellsten und verlässlichsten Informationen.

## 🙏 Danksagung

Ein großes Dankeschön an die Entwickler und Betreiber der [Feiertage-API](https://feiertage-api.de) für das Bereitstellen dieser großartigen Ressource. Bitte erwägen Sie, die ursprünglichen Entwickler zu unterstützen, indem Sie ihnen eine Spende zukommen lassen.
