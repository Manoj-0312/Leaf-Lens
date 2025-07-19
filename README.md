# Leaf Lens

## Installation

1. Clone the repository:
```
git clone https://github.com/your-username/leaf-lens.git
```
2. Navigate to the project directory:
```
cd leaf-lens
```
3. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
4. Install the required dependencies:
```
pip install -r requirements.txt
```
5. Set up the database:
```
flask db upgrade
```

## Usage

1. Start the Flask development server:
```
flask run
```
2. Open your web browser and navigate to `http://localhost:5000/`.

## API

The application provides the following API endpoints:

- `GET /get_fruit`: Retrieves the market prices for all fruits.
- `GET /get_vegetables`: Retrieves the market prices for all vegetables.
- `POST /predict`: Accepts an image file and predicts the disease or health status of the plant.

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

## License

This project is licensed under the [MIT License](LICENSE).

