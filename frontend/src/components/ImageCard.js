/* eslint-disable prettier/prettier */
import React from 'react';
import { Card, Button } from 'react-bootstrap';

const ImageCard = ({ image, deleteImage }) => {
  console.log('image ', image);
  return (
    <Card style={{ width: '18rem' }}>
      <Card.Img variant="top" src={image.data.urls.small} />
      <Card.Body>
        <Card.Title>{image.title.toUpperCase()}</Card.Title>
        <Card.Text>{image.data.description || image.data.alt_description}</Card.Text>
        <Button
          variant="primary"
          onClick={() => deleteImage(image.data.id)}
        >
          Delete
        </Button>
      </Card.Body>
    </Card>
  );
};

export default ImageCard;
