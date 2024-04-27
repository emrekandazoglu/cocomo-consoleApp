const calculateButton = document.getElementById('calculate-button');
const totalResult = document.getElementById('total-result');
const totalTcfElement = document.getElementById('total-tcf');
let total = 0; // total değişkenini global olarak tanımla
let totalTcf = 0; // totalTcf değişkenini global olarak tanımla
let IslevNoktasi = 0;

calculateButton.addEventListener('click', () => {
	total = 0; // her tıklamada sıfırla
	totalTcf = 0; // her tıklamada sıfırla

	// İlk tablodan verileri topla
	const table1Rows = document.querySelectorAll('table.table-bordered tbody tr');
	for (const row of table1Rows) {
		const userInput = parseFloat(row.querySelector('.user-input').value);
		const checkedOption = row.querySelector('input[type="checkbox"]:checked');

		if (userInput && checkedOption) {
			const selectedValue = parseFloat(checkedOption.value);
			const product = userInput * selectedValue;
			total += product;
		} else {
			alert('Lütfen her satırda bir sayı girin ve bir seçenek seçin.');
			return; // Hata varsa fonksiyondan çık
		}
	}

	// İkinci tablodan verileri topla
	const inputs = document.querySelectorAll('input[type="number"]');
	for (const input of inputs) {
		totalTcf += parseInt(input.value);
	}

	// Toplam sonucu göster
	totalResult.textContent = `Toplam Değer: ${total}`;
	// Toplam TCF'yi göster
	totalTcfElement.textContent = `Toplam TCF: ${totalTcf}`;

	IslevNoktasi = calculateIslevNoktasi(total, totalTcf);
	console.log('İşlev Noktası: ' + IslevNoktasi);
});

const inputs = document.querySelectorAll('input[type="number"]');

inputs.forEach(input => {
	input.addEventListener('change', () => {
		calculateTcf();
	});
});

function calculateTcf() {
	totalTcf = 0; // her değişiklikte sıfırla
	for (const input of inputs) {
		totalTcf += parseInt(input.value);
	}
	totalTcfElement.textContent = `Toplam TCF: ${totalTcf}`;
}

function calculateIslevNoktasi(total, totalTcf) {
	return total * (0.65 + 0.01 * totalTcf);
}

let a = function calculateMultiplier(
	IslevNoktasi1 = calculateIslevNoktasi(total, totalTcf),
	selectedLanguage
) {
	let multiplier = IslevNoktasi1;

	switch (selectedLanguage) {
		case 'Assembly':
			multiplier = 300;
			break;
		case 'Cobol':
			multiplier = 100;
			break;
		case 'Fortran':
			multiplier = 100;
			break;
		case 'Pascal':
			multiplier = 90;
			break;
		case 'C':
			multiplier = 90;
			break;
		case 'Ada':
			multiplier = 70;
			break;
		case 'NesneKokenliDiller':
			multiplier = 30;
			break;
		case '4KusakDilleri':
			multiplier = 20;
			break;
		case 'KodUreticiler':
			multiplier = 15;
			break;
		default:
			multiplier = 0;
			break;
	}

	return multiplier * selectedLanguage;
};

console.log(a()); // Fonksiyonu çağırarak sonucu yazdır
