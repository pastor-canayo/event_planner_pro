let slideIndex = 0;

function showSlides(){
	let i;
	const images = document.getElementsByClassName("slide");
	
	for(i = 0; i < images.length; i++){
		images[i].style.display = 'none';
	}
	slideIndex++;

	if(slideIndex > images.length){
		slideIndex = 1;
	}
	images[slideIndex - 1].style.display = 'block';

	setTimeout(showSlides, 3000); // change image every 2 secodns
}
showSlides();