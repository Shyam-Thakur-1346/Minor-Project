import fitz
import os

doc = fitz.open('C:/Users/shyam/Documents/Presentation format.pdf')
print('Page count:', len(doc))

for i, page in enumerate(doc):
    print(f'=== Page {i+1} ===')
    print('Rect:', page.rect)
    imgs = page.get_images(full=True)
    for idx, img in enumerate(imgs):
        xref = img[0]
        base = doc.extract_image(xref)
        ext = base['ext']
        path = f'C:/Users/shyam/Documents/student-skills-placement-tracker/format_img_{i+1}_{idx}.{ext}'
        with open(path, 'wb') as f:
            f.write(base['image'])
        print(f"Image saved: {path} ({base['width']}x{base['height']})")
    drawings = page.get_drawings()
    print(f'Drawings: {len(drawings)}')
    for d in drawings:
        print(' Drawing rect:', d.get('rect'), 'fill:', d.get('fill'), 'color:', d.get('color'))
    for block in page.get_text('dict')['blocks']:
        if 'lines' in block:
            for line in block['lines']:
                for span in line['spans']:
                    print(f"   font: {span['font']}, size: {span['size']:.1f}, text: {repr(span['text'])}")
