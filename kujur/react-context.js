import React from 'react';
import PhotosContext from './PhotosContext';
import ThemeContext from './ThemeContext';

const withTheme = WrappedComponent => {
  function WithTheme(props) {
    return (
      <ThemeContext.Consumer>
        {({ theme }) => (
          <WrappedComponent
            {...props}
            theme={theme}
          />
        )}
      </ThemeContext.Consumer>
    );
  }

  return WithTheme;
};

const withPhotos = WrappedComponent => {
  function WithPhotos(props) {
    return (
      <PhotosContext.Consumer>
        {({ photos, fetchPhotos }) => (
          <WrappedComponent
            {...props}
            photos={photos}
            fetchPhotos={fetchPhotos}
          />
        )}
      </PhotosContext.Consumer>
    );
  }

  return WithPhotos;
};

function PhotosList({ theme, photos = [], fetchPhotos }) {
  return (
    <div id='photos-list-container' style={{ background: theme === 'light' ? 'white' : 'black' }}>
      <ul id='photos-list'>
        {photos.map(({ title, imgSrc }, index) => (
          <li key={`photo-${index}`}>
            <h3 style={{ color: theme === 'light' ? 'black' : 'white' }} >{title}</h3>
            <img src={imgSrc}></img>
          </li>
        ))}
      </ul>
      <button id='fetch-photos' onClick={fetchPhotos} >Fetch photos</button>
    </div>
  )
}

export default withTheme(withPhotos(PhotosList));