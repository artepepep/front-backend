import Slider from '@/shared/components/Slider/Slider';
import productsData from '@/shared/data/products-data';

export default function ProductsList() {
  return (
    <div className="relative">
      <Slider data={productsData} />
    </div>
  );
}
